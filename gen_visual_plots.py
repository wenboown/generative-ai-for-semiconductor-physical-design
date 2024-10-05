import os
from collections import defaultdict
import yaml
import re

def latex_escape(text):
    """
    Escape special LaTeX characters in the given text.
    """
    special_chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
    }
    return ''.join(special_chars.get(c, c) for c in text)

def generate_question_tables(questions):
    latex = ""

    categories = {
        'basic_shapes_1': [
                        'Circle', 'Donut', 
                           'Oval', 
                           'Square', 'Triangle', 'Grid'
                           ],
        'basic_shapes_2': ['Hexagon', 
                           'Pentagon', 'Heptagon', 'Octagon', 'Trapezoid', 'Text'
                           ],
        'advanced_shapes': ['Arrow', 
                            'SquareArray', 
                            'Serpentine', 'RoundedSquare', 
                            'BasicLayout', 
                            'Spiral'
                            ],
        'complex_structures': [
            'MicrofluidicChip', 'ViaConnection', 
                               'FiducialCircle', 'ComplexLayout',
                               'DLDChip', 
                               'FinFET', 
                               'RectangleWithText'
                               ]
    }
    for category, shapes in categories.items():
        latex += f"\\begin{{table}}[htbp]\n"
        latex += f"\\caption{{{category.replace('_', ' ').title()} Questions}}\n"
        latex += f"\\label{{table:questions-{category.lower().replace(' ', '-')}}}\n"
        latex += "\\begin{tabularx}{\\textwidth}{@{}lX@{}}\n"
        latex += "\\hline\n"
        latex += "\\textbf{Shape} & \\textbf{Question} \\\\ \\hline\n"

        for question in questions:
            shape = question['context'].replace('.gds', '')
            if shape in shapes:
                escaped_question = latex_escape(question['question'])
                latex += f"{shape} & {escaped_question} \\\\ \\hline\n"
            elif category == "Other" and not any(shape in cat_shapes for cat_shapes in categories.values()):
                escaped_question = latex_escape(question['question'])
                latex += f"{shape} & {escaped_question} \\\\ \\hline\n"

        latex += "\\end{tabularx}\n"
        latex += "\\end{table}\n\n"

    return latex


def generate_latex_image_table(image_paths, llms, runs, groups, pool_experiments, questions):
    latex = ""
    
    short_names = {
        "gpt-4o": "GPT-4o",
        "o1-preview": "o1-preview",
        "claude-3-5-sonnet-20240620": "Claude-3.5",
        "watsonx_meta-llama_llama-3-1-70b-instruct": "Llama-3-70B",
        "watsonx_meta-llama_llama-3-405b-instruct": "Llama-3-405B"
    }
    
    for group_name, shapes in groups.items():
        for shape in shapes:
            if f"{shape}.png" not in image_paths:
                continue

            image_width = 0.13
            llm_data = image_paths[f"{shape}.png"]
            
            latex += "\\begin{table}\n"
            # Find the corresponding question
            question = next((q['question'] for q in questions if q['context'] == f"{shape}.gds"), "")
            if question:
                escaped_question = latex_escape(question)
                latex += f"  \\caption{{{shape} Task Question: {escaped_question}}}\n"
            latex += "  \\label{table:" + shape.lower() + "}\n"
            latex += "  \\centering\n"
            latex += "  \\begin{tabularx}{0.9\\textwidth}{@{}XXXXXX@{}}\n"
            latex += "    \\toprule\n"
            # Ground truth and SOLOMON results
            latex += f"    \\begin{{tabular}}{{@{{}}c@{{}}}}Ground Truth \\\\ \\includegraphics[width={image_width}\\textwidth]{{examples_png/{shape}.png}}\\end{{tabular}}"
            
            latex += " & GPT-4o & Claude-3.5 & Llama-3-70B & Llama-3-405B & o1-preview \\\\\n"
            latex += "    \\midrule\n"
            

            
            latex += "    SOLOMON"
            for llm in llms:
                if "pool_all" in llm_data.get(llm, {}).get('pool', {}):
                    latex += f" & \\includegraphics[width={image_width}\\textwidth]{{{llm_data[llm]['pool']['pool_all']}}}"
                else:
                    latex += " & "
            latex += " \\\\\n"
            
            # LLM results for 5 runs
            for run in runs:
                latex += f"    \\begin{{tabular}}{{@{{}}c@{{}}}}Single LLM \\\\ Baseline \\\\ Run {run}\\end{{tabular}}"
                for llm in llms:
                    if run in llm_data.get(llm, {}).get('run', {}):
                        latex += f" & \\includegraphics[width={image_width}\\textwidth]{{{llm_data[llm]['run'][run]}}}"
                    else:
                        latex += " & "
                latex += " \\\\\n"
            
            latex += "    \\bottomrule\n"
            latex += "  \\end{tabularx}\n"
            
            latex += "\\end{table}\n\n"

    return latex

def get_image_paths(base_path, llms, runs, pool_experiments):
    image_paths = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for run in runs:
        for llm in llms:
            run_path = f"{base_path}/run_{run}/png/{llm}_results"
            if os.path.exists(run_path):
                for file in os.listdir(run_path):
                    if file.endswith('.png'):
                        image_paths[file][llm]['run'][run] = f"{run_path}/{file}"
    
    # Handle pool folders
    for experiment in pool_experiments:
        for llm in llms:
            if 'o1-preview' in llm and 'pool' in experiment:
                continue  # Skip pool for o1-preview
            pool_path = f"{base_path}/{experiment}/png/{llm}_results"
            if os.path.exists(pool_path):
                for file in os.listdir(pool_path):
                    if file.endswith('.png'):
                        image_paths[file][llm]['pool'][experiment] = f"{pool_path}/{file}"
    
    return image_paths

def generate_markdown_table(image_paths, llms, runs, groups, pool_experiments):
    markdown = ""
    
    # Create a dictionary to map full LLM names to shorter versions
    short_names = {
        "gpt-4o": "GPT-4o",
        "claude-3-5-sonnet-20240620": "Claude-3.5-Sonnet",
        "watsonx_meta-llama_llama-3-1-70b-instruct": "Llama-3.1-70B",
        "watsonx_meta-llama_llama-3-405b-instruct": "Llama-3.1-405B",
        "o1-preview": "o1-preview",
    }
    
    for group_name, shapes in groups.items():
        markdown += f"## {group_name.replace('_', ' ').title()}\n\n"
        markdown += "| Shape & Run | Example | " + " | ".join(short_names[llm] for llm in llms) + " |\n"
        markdown += "|-------------|---------|" + "|".join(["-----" for _ in range(len(llms))]) + "|\n"

        for shape in shapes:
            if f"{shape}.png" not in image_paths:
                continue  # Skip shapes that don't have corresponding images
            
            llm_data = image_paths[f"{shape}.png"]
            example_img = f"<img src='/examples_png/{shape}.png' style='max-width:300px; max-height:300px;'>"
            
            # Handle run rows
            for run in runs:
                markdown += f"| **{shape}**<br>Run {run} | {example_img} |"
                for llm in llms:
                    if run in llm_data.get(llm, {}).get('run', {}):
                        markdown += f" <img src='/{llm_data[llm]['run'][run]}' style='max-width:300px; max-height:300px;'> |"
                    else:
                        markdown += " |"
                markdown += "\n"
            
            # Handle pool rows
            for experiment in pool_experiments:
                markdown += f"| **{shape}**<br>{experiment} | {example_img} |"
                for llm in llms:
                    if 'o1-preview' in llm:
                        markdown += " |"
                    elif experiment in llm_data.get(llm, {}).get('pool', {}):
                        markdown += f" <img src='/{llm_data[llm]['pool'][experiment]}' style='max-width:300px; max-height:300px;'> |"
                    else:
                        markdown += " |"
                markdown += "\n"
            
            markdown += "| | | " + " | ".join(["" for _ in llms]) + " |\n"

        markdown += "\n"  # Add extra newline between groups

    return markdown

def main():
    base_path = "."  # Adjust this if needed
    llms = ["gpt-4o", "o1-preview", "claude-3-5-sonnet-20240620", "watsonx_meta-llama_llama-3-1-70b-instruct",
            "watsonx_meta-llama_llama-3-405b-instruct"]
    runs = range(1, 6)  # 5 runs
    pool_experiments = [
        "pool_all"
    ]

    groups = {
        'basic_shapes_1': [
                           'Circle', 'Donut', 
                           'Oval', 
                           'Square', 'Triangle', 'Grid'
                           ],
        'basic_shapes_2': ['Hexagon', 
                           'Pentagon', 'Heptagon', 'Octagon', 'Trapezoid', 'Text'
                           ],
        'advanced_shapes': ['Arrow', 
                            'SquareArray', 
                            'Serpentine', 'RoundedSquare', 
                            'BasicLayout', 
                            'Spiral'
                            ],
        'complex_structures': [
                            'MicrofluidicChip', 
                            'ViaConnection', 
                            'FiducialCircle', 
                            'ComplexLayout',
                            'DLDChip', 
                            'FinFET', 
                            'RectangleWithText'
                            ]
    }
    
    with open("example_questions.yaml", "r") as f:
        questions = yaml.safe_load(f)['context_questions']

    image_paths = get_image_paths(base_path, llms, runs, pool_experiments)
    latex_tables = generate_latex_image_table(image_paths, llms, runs, groups, pool_experiments, questions)
    

    # with open("plot_experiment.tex", "w") as f:
    #     f.write(latex_tables)
    
    # # Add this line to generate the question tables
    # question_tables = generate_question_tables(questions)

    # with open("table_questions.tex", "w") as f:
    #     f.write(question_tables)

    markdown_table = generate_markdown_table(image_paths, llms, runs, groups, pool_experiments)

    with open("plot_experiment.md", "w") as f:
        f.write(markdown_table)

if __name__ == "__main__":
    main()