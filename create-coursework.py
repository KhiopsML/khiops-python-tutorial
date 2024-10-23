#! /usr/bin/python

import glob
import json
import os
import shutil


def main():
    print("Creating coursework dir ...")
    coursework_dir_path = os.path.join(".", "coursework")
    if os.path.exists(coursework_dir_path):
        shutil.rmtree(coursework_dir_path)
    os.mkdir(coursework_dir_path)

    print("Creating resources ...")
    data_dir_path = os.path.join(".", "data")
    coursework_data_dir_path = os.path.join(coursework_dir_path, "data")
    shutil.copytree(data_dir_path, coursework_data_dir_path)

    print("Creating notebooks ...")
    notebooks_glob = os.path.join(".", "*.ipynb")
    for input_notebook_path in glob.glob(notebooks_glob):
        output_notebook_path = os.path.join(
            coursework_dir_path, os.path.basename(input_notebook_path)
        )

        print(input_notebook_path, " -> ", output_notebook_path)
        create_notebook_without_solutions(input_notebook_path, output_notebook_path)


def create_notebook_without_solutions(input_notebook_path, output_notebook_path):
    with open(input_notebook_path, encoding="utf8") as input_notebook_file, open(
        output_notebook_path, "w"
    ) as output_notebook_file:
        notebook = json.load(input_notebook_file)
        cells = notebook["cells"]
        for cell in cells:
            metadata = cell["metadata"]
            if "is_khiops_tutorial_solution" in metadata:
                cell["source"] = []

        json.dump(notebook, output_notebook_file)


if __name__ == "__main__":
    main()
