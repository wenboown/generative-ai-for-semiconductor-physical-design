import os
import json
from collections import defaultdict
from yaml2gds import load_yaml_to_dict

def load_examples_and_results(base_dir, yaml_file):
    # Load examples from YAML
    examples = load_yaml_to_dict(yaml_file)
    
    # Initialize result dictionary
    result = defaultdict(lambda: defaultdict(dict))

    # Iterate through run folders
    for run_folder in os.listdir(base_dir):
        if not run_folder.startswith('run_'):
            continue

        run_path = os.path.join(base_dir, run_folder, 'gds')
        for llm_folder in os.listdir(run_path):
            if not llm_folder.endswith('_results'):
                continue

            llm_type = llm_folder.rsplit('_', 1)[0]
            llm_path = os.path.join(run_path, llm_folder)
            
            # Process .py and .err files
            for context in examples.keys():
                # Remove .gds extension if present
                context_base = context[:-4] if context.endswith('.gds') else context
                py_file = f"{context_base}.py"
                err_file = f"{context_base}.err"
                # Load .py file content
                py_path = os.path.join(llm_path, py_file)
                fixed_py_file = f"{context_base}_fixed_LayoutViewer.py"
                fixed_py_path = os.path.join(llm_path, fixed_py_file)
                
                if os.path.exists(py_path):
                    with open(py_path, 'r') as f:
                        py_content = f.read().strip()
                elif os.path.exists(fixed_py_path):
                    with open(fixed_py_path, 'r') as f:
                        py_content = f.read().strip()
                else:
                    py_content = "File not found"

                # Load .err file content or set to "no error"
                err_path = os.path.join(llm_path, err_file)
                fixed_err_file = f"{context_base}_fixed_LayoutViewer.err"
                fixed_err_path = os.path.join(llm_path, fixed_err_file)
                if os.path.exists(err_path):
                    with open(err_path, 'r') as f:
                        err_content = f.read().strip()
                elif os.path.exists(fixed_err_path):
                    with open(fixed_err_path, 'r') as f:
                        err_content = f.read().strip()
                else:
                    err_content = "no error"

                # Add to result dictionary
                result[context][run_folder][llm_type] = {
                    'py_content': py_content,
                    'err_content': err_content,
                    'image_path': os.path.join(llm_path.replace('gds', 'png'), f"{context_base}.png")
                }

    # Combine examples and results
    for context, data in examples.items():
        data['results'] = result[context]

    return examples

def generate_report(combined_data):
    report = defaultdict(lambda: defaultdict(int))
    
    for context, data in combined_data.items():
        for run_folder, run_data in data['results'].items():
            report[context][run_folder] = len(run_data)
    
    print("\nDetailed Report:")
    print("----------------")
    for context, run_counts in report.items():
        print(f"\nTask: {context}")
        for run, count in run_counts.items():
            print(f"  {run}: {count} py_content entries")
        
        # Check if all runs have 5 py_content entries
        if all(count == 5 for count in run_counts.values()):
            print("  All runs have 5 py_content entries as expected.")
        else:
            print("  Warning!!: Not all runs have 5 py_content entries!")

def main():
    base_dir = '.'  # Assuming the script is run from the directory containing run_x folders
    yaml_file = 'examples.yaml'  # Update this path if necessary
    
    combined_data = load_examples_and_results(base_dir, yaml_file)
    
    # Save as JSON
    with open('combined_results.json', 'w') as f:
        json.dump(combined_data, f, indent=2)
    
    print("Combined data saved in combined_results.json")
    # Generate and print the detailed report
    generate_report(combined_data)
if __name__ == "__main__":
    main()