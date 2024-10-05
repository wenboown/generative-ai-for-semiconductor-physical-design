import litellm
import yaml
from typing import Dict, Any, List, Tuple
from dotenv import load_dotenv
import os
from yaml2gds import load_yaml_to_dict
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI
client = OpenAI()

load_dotenv()

def save_yaml(data: Dict[str, Any], file_path: str):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def load_system_prompt(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read().strip()

def get_completed_examples(output_file: str) -> List[str]:
    if os.path.exists(output_file):
        data = load_yaml_to_dict(output_file)
        return [example['context'] for example in data.get('seed_examples', [])]
    return []

def process_single_example(llm: str, filename: str, content: Dict[str, str], system_prompt: str, run_dir: str) -> Tuple[str, Dict[str, Any]]:
    output_file = os.path.join(run_dir, f"{llm.replace('/', '_')}_results.yaml")
    print(f"Processing {llm} - {filename}...")
    try:
        if "o1-" not in llm:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": content['question'].strip()}
            ]
            res = litellm.completion(messages=messages, model=llm, max_tokens=2000)
        else:
            messages = [
                {"role": "user", "content": system_prompt + "\n\n" + content['question'].strip()}
            ]
            res = client.chat.completions.create(model=llm, messages=messages)
        response = res.choices[0].message.content
        usage = res.usage
        # Convert usage to a simple dictionary
        usage_dict = {
            'prompt_tokens': usage.prompt_tokens,
            'completion_tokens': usage.completion_tokens,
            'total_tokens': usage.total_tokens,
            'reasoning_tokens': usage.completion_tokens_details.get('reasoning_tokens', 0),
        }
        result = {
            'context': filename,
            'question': content['question'],
            'answer': response,
            'usage': usage_dict
        }
        return llm, result
    except Exception as e:
        print(f"Error processing {llm} - {filename}: {str(e)}")
        return llm, None

def process_examples(llms: List[str], input_file: str, system_prompt: str, num_runs: int):
    input_data = load_yaml_to_dict(input_file)

    for run in range(num_runs):
        run_dir = f"run_{run + 1}"
        os.makedirs(run_dir, exist_ok=True)

        # Initialize output data for all LLMs
        output_data = {llm: {
            'version': 2,
            'task_description': f'Generate Python code for GDS shapes using {llm}',
            'created_by': f'{llm}',
            'seed_examples': []
        } for llm in llms}

        # Load existing results
        for llm in llms:
            output_file = os.path.join(run_dir, f"{llm.replace('/', '_')}_results.yaml")
            if os.path.exists(output_file):
                output_data[llm] = load_yaml_to_dict(output_file)

        # Process examples in parallel
        with ThreadPoolExecutor(max_workers=len(llms)) as executor:
            for filename, content in input_data.items():
                if all(filename in [ex['context'] for ex in output_data[llm]['seed_examples']] for llm in llms):
                    print(f"Skipping {filename} (already processed by all LLMs)")
                    continue

                futures = [executor.submit(process_single_example, llm, filename, content, system_prompt, run_dir) for llm in llms]
                for future in concurrent.futures.as_completed(futures):
                    llm, result = future.result()
                    if result:
                        output_data[llm]['seed_examples'].append(result)

        # Save results for all LLMs
        for llm in llms:
            output_file = os.path.join(run_dir, f"{llm.replace('/', '_')}_results.yaml")
            save_yaml(output_data[llm], output_file)
            print(f"Saved results for {llm} (Run {run + 1})")

        print(f"Completed processing for Run {run + 1}")

    print("Processing complete.")

# Main execution
if __name__ == "__main__":
    system_prompt = load_system_prompt('prompt.txt')
    input_file = 'examples.yaml'
    llms = [
        # "gpt-4o",
        "o1-preview",
        # "claude-3-5-sonnet-20240620",
        # "watsonx/meta-llama/llama-3-1-70b-instruct",
        # "watsonx/meta-llama/llama-3-405b-instruct"
    ]
    num_runs = 5

    process_examples(llms, input_file, system_prompt, num_runs)
