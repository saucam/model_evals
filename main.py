import argparse
import json
import logging
import os
import time
import math
import os
import requests
import base64

from pytablewriter import MarkdownTableWriter

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

def _make_summary(directory: str, model_name: str, benchmark: str) -> str:
    # Variables
    tables = []
    averages = []
    tasks = []
    for test_file in os.listdir(directory):
        test_file_path = os.path.join(directory, test_file)
        if test_file.endswith('.json'):
            task, _ = os.path.splitext(test_file)
            json_data = open(test_file_path, "r").read()
            data = json.loads(json_data, strict=False)
            table, average = make_table(data, task, benchmark)
            tables.append(table)
            tasks.append(task)
            averages.append(average)
    # Generate tables
    summary = ""
    for index, task in enumerate(tasks):
        summary += f"### {task}\n{tables[index]}\nAverage: {averages[index]}%\n\n"
    result_dict = {k: v for k, v in zip(tasks, averages)}

    # Calculate the final average, excluding strings
    if all(isinstance(e, float) for e in averages):
        final_average = round(sum(averages) / len(averages), 2)
        summary += f"Average score: {final_average}%"
        result_dict.update({"Average": final_average})
    else:
        summary += "Average score: Not available due to errors"

    # Generate final table
    final_table = make_final_table(result_dict, model_name)
    summary = final_table + "\n" + summary

    # Read elapsed time from json
    
    return summary

    # Tasks
    # if BENCHMARK == "openllm":
    #     tasks = ["ARC", "HellaSwag", "MMLU", "TruthfulQA", "Winogrande", "GSM8K"]
    # elif BENCHMARK == "nous":
    #     tasks = ["AGIEval", "GPT4All", "TruthfulQA", "Bigbench"]
    # elif BENCHMARK == "eq-bench":
    #     tasks = ["EQ-Bench"]
    # else:
    #     raise NotImplementedError(
    #         f"The benchmark {BENCHMARK} could not be found."
    #     )

def make_final_table(result_dict, model_name):
    """Generate table of results with model name.

    Args:
    result_dict (dict): A dictionary where keys are headers and values are the values in the table.
    model_name (str): The name of the model to be included in the table.

    Returns:
    str: A string representing the markdown table.
    """
    md_writer = MarkdownTableWriter()
    # Add 'Model' as the first header and then the rest from the dictionary keys
    md_writer.headers = ["Model"] + list(result_dict.keys())

    # The values in the table will be the model name and then the values from the dictionary
    values = [
        f"[{model_name.split('/')[-1]}](https://huggingface.co/{model_name})"
    ] + list(result_dict.values())

    # The table only has one row of values
    md_writer.value_matrix = [values]

    # Return the table as a markdown formatted string
    return md_writer.dumps()

def get_acc_norm(data):
    accs = [
        data["results"][k]["acc_norm"]
        if "acc_norm" in data["results"][k]
        else data["results"][k]["acc"]
        for k in data["results"]
    ]
    acc = sum(accs) / len(accs) * 100
    return acc


def get_mcg(data):
    accs = [data["results"][k]["multiple_choice_grade"] for k in data["results"]]
    acc = sum(accs) / len(accs) * 100
    return acc


def calculate_average(data, task, bench):
    task = task.lower()
    print(data)

    if bench == "openllm":
        if task == "arc":
            return data["results"]["arc_challenge"]["acc_norm,none"] * 100
        elif task == "hellaswag":
            return data["results"]["hellaswag"]["acc_norm,none"] * 100
        elif task == "mmlu":
            return data["results"]["mmlu"]["acc,none"] * 100
        elif task == "truthfulqa":
            value = data["results"]["truthfulqa_mc2"]["acc,none"]
            return 0.0 if math.isnan(value) else value * 100
        elif task == "winogrande":
            return data["results"]["winogrande"]["acc,none"] * 100
        elif task == "gsm8k":
            return data["results"]["gsm8k"]["exact_match,strict-match"] * 100

    elif bench == "nous":
        if task == "agieval":
            return get_acc_norm(data)
        elif task == "gpt4all":
            return get_acc_norm(data)
        elif task == "bigbench":
            return get_mcg(data)
        elif task == "truthfulqa":
            value = data["results"]["truthfulqa_mc"]["mc2"]
            return 0.0 if math.isnan(value) else value * 100

    elif bench == "eq-bench":
        if task == "eq-bench":
            return data["results"]["eq_bench"]["eqbench,none"]

    raise NotImplementedError(f"Could not find task {task} for benchmark {BENCHMARK}")


def make_table(result_dict, task, bench):
    """Generate table of results."""
    # TODO: properly format values in table for openllm

    md_writer = MarkdownTableWriter()
    md_writer.headers = ["Task", "Version", "Metric", "Value", "", "Stderr"]

    values = []

    for k, dic in sorted(result_dict["results"].items()):
        version = result_dict["versions"].get(k, "N/A")

        percent = k == "squad2"
        for m, v in dic.items():
            if m.endswith("_stderr"):
                continue

            if m + "_stderr" in dic:
                se = dic[m + "_stderr"]
                if percent or m == "ppl":
                    values.append([k, version, m, "%.2f" % v, "±", "%.2f" % se])
                else:
                    values.append(
                        [k, version, m, "%.2f" % (v * 100), "±", "%.2f" % (se * 100)]
                    )
            else:
                if percent or m == "ppl":
                    values.append([k, version, m, "%.2f" % v, "", ""])
                else:
                    try:
                        # Attempt to convert v to a float
                        v_converted = float(v)
                        v_formatted = "%.2f" % v_converted
                    except ValueError:
                        # If conversion fails, use the original string value
                        v_formatted = v

                    values.append([k, version, m, v_formatted, "", ""])

            k = ""
            version = ""

    md_writer.value_matrix = values

    # Get average score
    average = round(calculate_average(result_dict, task, bench), 2)

    return md_writer.dumps(), average

def upload_file_to_github(token, repo_owner, repo_name, file_path, file_content, commit_message):
    """
    Uploads a file to a GitHub repository. If the file already exists, it replaces it.

    Parameters:
    - token: Personal Access Token (PAT) for GitHub with the appropriate scopes.
    - repo_owner: Username of the repository owner.
    - repo_name: Name of the repository.
    - file_path: Path where the file will be stored in the repository (including filename).
    - file_content: Content of the file to upload.
    - commit_message: Commit message for the file upload.

    Returns:
    - Response from the GitHub API.
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

    # Encode file content to base64
    encoded_content = base64.b64encode(file_content.encode("utf-8")).decode("utf-8")

    # Prepare headers
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Prepare data
    data = {
        "message": commit_message,
        "content": encoded_content,
    }

    # Check if file exists
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # File exists, update it
        data["sha"] = response.json()["sha"]  # Include the SHA of the file to update

    # Make the PUT request to create or update the file
    response = requests.put(url, headers=headers, json=data)
    return response.json()  # Return the JSON response

def upload_to_github_gist(text, gist_name, gh_token):
    # Create the gist content
    gist_content = {
        "public": str(os.getenv("PRIVATE_GIST", False)).lower(),
        "files": {
            f"{gist_name}": {  # Change the file extension to .txt for plain text
                "content": text
            }
        },
    }

    # Headers for the request
    headers = {
        "Authorization": f"token {gh_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Make the request
    response = requests.post(
        "https://api.github.com/gists", headers=headers, json=gist_content
    )

    if response.status_code == 201:
        print(f"Uploaded gist successfully! URL: {response.json()['html_url']}")
    else:
        print(
            f"Failed to upload gist. Status code: {response.status_code}. Response: {response.text}"
        )

def main(directory: str, model_name: str) -> str:
    # model_name = os.path.basename(directory)
    print(f"model name = {model_name}")
    for benchmark in os.listdir(directory):
        benchmark_path = os.path.join(directory, benchmark)
        if os.path.isdir(benchmark_path):
            # Tasks
            summary = _make_summary(directory=benchmark_path, model_name=model_name, benchmark=benchmark)
            metadata_path = os.path.join(directory, f"summary_{benchmark}.json")
            json_data = open(metadata_path, "r").read()
            data = json.loads(json_data, strict=False)
            summary += f"\n\nMetadata: {data}"
            return summary

            # upload_to_github_gist(
            #     summary,
            #     f"{model_name}-{benchmark.capitalize()}.md",
            #     GITHUB_API_TOKEN,
            # )

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Summarize results and upload them.")
    parser.add_argument(
        "directory", type=str, help="The path to the directory with the JSON results"
    )
    # parser.add_argument(
    #     "elapsed_time",
    #     type=float,
    #     help="Elapsed time since the start of the evaluation",
    # )

    # Parse the arguments
    args = parser.parse_args()

    # Check if the directory exists
    if not os.path.isdir(args.directory):
        raise ValueError(f"The directory {args.directory} does not exist.")

    # Call the main function with the directory argument
    summary = f"# Model Eval results\n\n"
    for user_name in os.listdir(args.directory):
        username_path = os.path.join(args.directory, user_name)
        if os.path.isdir(username_path):
            for model_name in os.listdir(username_path):
                model_path = os.path.join(username_path, model_name)
                print(model_path)
                if os.path.isdir(model_path):
                    summary += main(model_path, f"{user_name}/{model_name}")
    upload_file_to_github(GITHUB_API_TOKEN, "saucam", "model_evals", "README.md", summary, "Update Readme")        
