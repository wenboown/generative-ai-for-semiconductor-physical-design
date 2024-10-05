# LLM for Layout Design

This repository contains the code for the paper: "Enhancing Reasoning to Adapt Large Language Models for Domain-Specific Applications", submitted to [NeurIPS 2024 Workshop on Adaptive Foundation Models](https://adaptive-foundation-models.org).

## Overview

We release the complete benchmark dataset of 25 tasks and LLM API calling code under the Apache 2.0 license. This repository includes 5 runs of results (LLM answers, Python code, error logs, and PNGs) for each task in the baseline experiment for reproducibility.

## Requirements

- Python 3.11

## Repository Contents

1. `examples.yaml`: Contains 25 tasks and their ground truth code.
2. `example_questions.yaml`: A version containing only the questions (prompts).
3. `prompt.txt`: The system prompt for baseline experiment.
4. `yaml2gds.py`: Generates corresponding GDS, Python, and error log files from a yaml file.
5. `gds2png.py`: Generates PNG images from GDS with scale bar text.
6. `basic_experiments.py`: Generates baseline experiment results and output YAMLs in run folders.
7. `runs2png.py`: Generates GDS, Python, error, and PNG images for all runs.
8. `gen_visual_plots.py`: Creates `plot_experiment.md` for visualizing results for human evaluation.
9. `analysis_err.py`: Generates error reports from the runs.

## Setup and Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/wenboown/generative-ai-for-semiconductor-physical-design.git
   cd generative-ai-for-semiconductor-physical-design
   ```

2. Set up the environment:
   - `pip install -r requirements.txt`
   - Copy `env_example` to `.env` and provide your API keys.

3. Generate GDS files:
   - Check the path in `__main__` of `yaml2gds.py`
   - Run: `python yaml2gds.py`

4. Generate PNG images:
   - Check the path in `__main__` of `gds2png.py`
   - Run: `python gds2png.py`

5. Run baseline experiments:
   ```bash
   python basic_experiments.py
   python runs2png.py
   python gen_visual_plots.py
   python analysis_err.py
   ```

6. Human evaluation:
   - Inspect `plot_experiment.md` on GitHub (which will render the images)
   - Enter the information into `plots/test_result.csv`
   - (Optional) use the `figure.ipynb` to plot the results.

## LLM Experiments

- APIs used: GPT-4 (OpenAI), Claude (Anthropic), and Llama 3 (IBM Watsonx)
- Total API costs: Approximately $50 (including re-runs and iterative testing)

## SOLOMON Code

SOLOMON code is proprietary at this moment. Its experiment results are included in the `pool_all` folder and analysis result in `plots/judge_result.csv`.

## Dataset and Reproducibility

The complete dataset, including prompts, ground truths, and LLM outputs, is available in this repository. This contains all materials needed to reproduce our baseline experiments and conduct further research.

## License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE)

## Contact

For any questions or concerns, please open an issue in this repository.
