import os
import json
import csv
from collections import defaultdict

def analyze_errors(base_dir):
    error_data = defaultdict(lambda: defaultdict(list))
    error_counts = defaultdict(lambda: defaultdict(int))

    for run_folder in os.listdir(base_dir):
        if not run_folder.startswith('run_'):
            continue

        run_path = os.path.join(base_dir, run_folder, 'gds')
        for llm_folder in os.listdir(run_path):
            if not llm_folder.endswith('_results'):
                continue

            llm_type = llm_folder.rsplit('_', 1)[0]
            llm_path = os.path.join(run_path, llm_folder)
            
            for file in os.listdir(llm_path):
                if file.endswith('.err'):
                    file_path = os.path.join(llm_path, file)
                    task_name = os.path.splitext(file)[0]
                    
                    with open(file_path, 'r') as f:
                        error_content = f.read().strip()
                        last_line = error_content.split('\n')[-1]
                    
                    error_data[llm_type][run_folder].append({
                        'task': task_name,
                        'error': last_line
                    })
                    error_counts[llm_type][last_line] += 1

    return error_data, error_counts

def save_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def save_as_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['LLM', 'Run', 'Task', 'Error'])
        for llm, runs in data.items():
            for run, errors in runs.items():
                for error_info in errors:
                    writer.writerow([llm, run, error_info['task'], error_info['error']])

def generate_report(error_counts, filename):
    with open(filename, 'w') as f:
        f.write("Error Analysis Report\n")
        f.write("=====================\n\n")
        
        for llm, errors in error_counts.items():
            f.write(f"LLM: {llm}\n")
            f.write("-" * (len(llm) + 5) + "\n")
            total_errors = sum(errors.values())
            f.write(f"Total errors: {total_errors}\n\n")
            
            for error, count in sorted(errors.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / total_errors) * 100
                f.write(f"- {error}: {count} ({percentage:.2f}%)\n")
            
            f.write("\n")

def main():
    base_dir = '.'  # Assuming the script is run from the directory containing run_x folders
    error_data, error_counts = analyze_errors(base_dir)
    
    save_as_json(error_data, 'error_data.json')
    save_as_csv(error_data, 'error_data.csv')
    generate_report(error_counts, 'error_report.txt')
    
    print("Analysis complete. Results saved in error_data.json, error_data.csv, and error_report.txt")

if __name__ == "__main__":
    main()