import yaml
import os
import re
import subprocess
import gdspy
import textwrap
import time
from typing import List, Dict, Any
import json
import tempfile
import shutil

def load_yaml_to_dict(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    result = {}
    for example in data['seed_examples']:
        context = example['context'].strip()
        result[context] = {
            'question': example['question'].strip(),
            'answer': example['answer'].strip()
        }

    return result


def create_error_gds(filename, error_message, output_folder):
    lib = gdspy.GdsLibrary()
    cell_name = f"ERROR_{output_folder}_{os.path.splitext(filename)[0]}"
    cell = lib.new_cell(cell_name)

    # Define text parameters
    text_size = 5  # Adjust this value to change text size
    line_spacing = 1.5  # Adjust this value to change line spacing
    max_width = 100  # Maximum width of text in GDS units

    # Define high layer numbers for error messages
    TEXT_LAYER = 999  # Layer for error text
    BG_LAYER = 1000   # Layer for error background

    # Wrap text
    wrapped_text = textwrap.wrap(error_message, width=50)  # Adjust width as needed

    # Create text elements
    text_elements = []
    for i, line in enumerate(wrapped_text):
        y_position = -i * text_size * line_spacing
        # Use TEXT_LAYER for text, which can be interpreted as red
        text = gdspy.Text(line, text_size, (0, y_position), layer=TEXT_LAYER, datatype=0)
        text_elements.append(text)

    # Calculate bounding box for all text elements
    all_bboxes = [text.get_bounding_box() for text in text_elements]
    min_x = min(bbox[0][0] for bbox in all_bboxes)
    min_y = min(bbox[0][1] for bbox in all_bboxes)
    max_x = max(bbox[1][0] for bbox in all_bboxes)
    max_y = max(bbox[1][1] for bbox in all_bboxes)

    # Create background
    padding = 10  # Adjust this value to change padding around text
    # Use BG_LAYER for background, which can be interpreted as yellow
    background = gdspy.Rectangle(
        (min_x - padding, min_y - padding),
        (max_x + padding, max_y + padding),
        layer=BG_LAYER, datatype=0
    )

    # Add background and text to cell
    cell.add(background)
    for text in text_elements:
        cell.add(text)

    # Save the GDSII file
    output_file = os.path.join(output_folder, filename)
    lib.write_gds(output_file)
    print(f"Created error GDS file: {output_file}")

def fix_layoutviewer_error(code):
    lines = code.split('\n')
    detected_layoutviewer = any('LayoutViewer' in line for line in lines)
    fixed_lines = [line for line in lines if 'LayoutViewer' not in line]
    return '\n'.join(fixed_lines), detected_layoutviewer

def run_and_monitor_gds_creation(code: str, output_folder: str, expected_filename: str) -> None:
    # Create a temporary directory to run the script, because the llm code might create unexpected output filenames.
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the code to a temporary file
        temp_file = os.path.join(temp_dir, "temp_script.py")
        code, detected_layoutviewer = fix_layoutviewer_error(code)
        with open(temp_file, 'w') as f:
            f.write(code)

        # Get the list of files in the temp directory before running the script
        before: List[str] = os.listdir(temp_dir)

        # Run the script
        result = subprocess.run(['python', temp_file],
                                cwd=temp_dir,
                                capture_output=True,
                                text=True)
        print(result.stdout)

        # Wait a short time to ensure all file operations are complete
        time.sleep(0.5)

        # Get the list of files in the temp directory after running the script
        after: List[str] = os.listdir(temp_dir)

        # Find new files
        new_files: List[str] = [f for f in after if f not in before]
        if detected_layoutviewer:
            output_filename = expected_filename.replace('.gds', '_fixed_LayoutViewer.gds')
        else:
            output_filename = expected_filename
        # Move GDS files to the output folder
        for file in new_files:
            if file.endswith('.gds'):
                src: str = os.path.join(temp_dir, file)
                dst: str = os.path.join(output_folder, output_filename)
                shutil.move(src, dst)
                print(f"Moved {file} to {output_folder} as {output_filename}")
        
        # Copy the temporary Python file to the output folder
        py_src: str = temp_file
        py_dst: str = os.path.join(output_folder, f"{os.path.splitext(output_filename)[0]}.py")
        shutil.copy(py_src, py_dst)
        print(f"Copied temp_script.py to {output_folder} as {os.path.splitext(output_filename)[0]}.py")

        return result


def extract_and_run_python_code(data, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename, content in data.items():
        try:
            code_blocks = re.findall(r'```(python|Python)?\s*(.*?)```', content['answer'], re.DOTALL | re.IGNORECASE)
            code_blocks = [block[1] for block in code_blocks]  # Extract the code content from the matched groups

            # Merge code blocks
            merged_code = '\n'.join(block.strip() for block in code_blocks)

            if not merged_code.strip():  # Check if the merged code is empty or just whitespace
                raise ValueError("No Python code found")

            print(f"Processing {filename}")
            result = run_and_monitor_gds_creation(merged_code, output_folder, filename)

            if result.returncode != 0:
                error_message = f"Error in {filename}:\n{result.stdout}\n{result.stderr}"
                print(error_message)
                create_error_gds(filename, error_message, output_folder)
                
                # Save error message to .err file
                err_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.err")
                with open(err_file, 'w') as f:
                    f.write(error_message)

        except Exception as e:
            error_message = f"Error in {filename}: {str(e)}"
            print(error_message)
            create_error_gds(filename, error_message, output_folder)
            
            # Save error message to .err file
            err_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.err")
            with open(err_file, 'w') as f:
                f.write(error_message)

def main(input_yaml, output_folder):
    data = load_yaml_to_dict(input_yaml)

    print("List of all GDS files:")
    for filename in data.keys():
        print(filename)

    extract_and_run_python_code(data, output_folder)


def is_gds_related(code: str) -> bool:
    gds_keywords = ['gdspy', 'GdsLibrary', 'write_gds', 'gdsCAD']
    return any(keyword in code for keyword in gds_keywords)


def create_non_gds_error_gds(filename: str, output_folder: str) -> None:
    error_message = "This Python code does not appear to be related to GDS generation."
    create_error_gds(filename, error_message, output_folder)


def process_json_item(item: Dict[str, Any], index: int, output_folder: str) -> None:
    filename = f"training_data_{index}.gds"

    try:
        code_blocks = re.findall(r'```(?:python|Python)?\s*(.*?)```', item['output'], re.DOTALL | re.IGNORECASE)

        # Merge code blocks
        merged_code = '\n'.join(block.strip() for block in code_blocks)

        if not merged_code.strip():  # Check if the merged code is empty or just whitespace
            raise ValueError("No Python code found")

        if not is_gds_related(merged_code):
            create_non_gds_error_gds(filename, output_folder)
            print(f"Created non-GDS error file for {filename}")
            return

        print(f"Processing {filename}")
        run_and_monitor_gds_creation(merged_code, output_folder, filename)

    except subprocess.CalledProcessError as e:
        error_message = f"Error in {filename}:\n{e.stdout}\n{e.stderr}"
        print(error_message)
        create_error_gds(filename, error_message, output_folder)
    except Exception as e:
        error_message = f"Error in {filename}: {str(e)}"
        print(error_message)
        create_error_gds(filename, error_message, output_folder)


def main_json(input_json: str, output_folder: str) -> None:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_json, 'r') as f:
        data = json.load(f)

    for index, item in enumerate(data):
        process_json_item(item, index, output_folder)


if __name__ == "__main__":
    input_yaml = 'examples.yaml'  # You can change this or add command-line arguments
    output_folder = 'examples_gds'  # You
    # can change this or add command-line arguments

    main(input_yaml, output_folder)
