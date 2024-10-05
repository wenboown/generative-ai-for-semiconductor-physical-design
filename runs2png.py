import os
import glob
import shutil
from concurrent.futures import ProcessPoolExecutor, wait
import multiprocessing
from yaml2gds import main as yaml2gds_main
from gds2png import main as gds2png_main

def process_yaml(run_folder, yaml_file):
    llm_name = os.path.splitext(os.path.basename(yaml_file))[0]
    gds_folder = os.path.join(run_folder, 'gds', llm_name)
    png_folder = os.path.join(run_folder, 'png', llm_name)

    # Create necessary folders
    os.makedirs(gds_folder, exist_ok=True)
    os.makedirs(png_folder, exist_ok=True)

    # Process YAML to GDS
    yaml2gds_main(yaml_file, gds_folder)

    # Process GDS to PNG
    gds2png_main(gds_folder, png_folder)

def main():
    # Get the number of CPUs
    num_cpus = multiprocessing.cpu_count()

    # Get the path of the plot.md file
    plot_md_path = os.path.join(os.path.dirname(__file__), 'plot.md')

    # Create a pool of workers
    with ProcessPoolExecutor(max_workers=num_cpus) as executor:
        # Find all run folders
        folders = glob.glob('run_*')
        # folders = glob.glob('pool_*')

        # List to store all submitted tasks
        futures = []

        for run_folder in folders:

            # Find all YAML files in the run folder
            yaml_files = glob.glob(os.path.join(run_folder, '*.yaml'))

            # Submit tasks to the executor and store the Future objects
            for yaml_file in yaml_files:
                future = executor.submit(process_yaml, run_folder, yaml_file)
                futures.append(future)

        # Wait for all tasks to complete
        wait(futures)

if __name__ == "__main__":
    main()
