# Khiops Python Tutorial Notebooks

This repository contains the `khiops-python` tutorial notebooks. Unlike the package documentation,
they are focused more on being pedagogical and less on being complete.

## How To Install the Repository for Developing
```bash
# Make sure you are a member of the pykhiops-tutorial Gitlab and that you have set up the SSH keys for Git
git clone git@github.com:khiopsml/khiops-python-tutorial.git

# Install pre-commit and set up the hooks
pip install -U pre-commit my-nb-clean
pre-commit install
```
The `nb-clean` hook is very important to have a *sane* repository of notebooks. It cleans the
output cells and metadata that varies a lot from computer to computer. We also have a customized
cleaning script `custom-nb-clean`.

## Creating the Coursework Materials (TP)

Running the `create-coursework.py` in the project's root generates a subfolder named `coursework`.
This subfolder will contain the notebooks for lessons but without the exercises' solutions.

The notebooks with solutions are aimed to the course's teacher while those without them are aimed
to the course students or to persons learning Khiops by themselves.

### How It Is Done?
Cells that are solutions to exercises contain the following metadata:
```json
{
    "is_khiops_tutorial_solution": true
}
```
script looks for this information and eliminates a cell that has the key
`is_khiops_tutorial_solution` when writing the coursework notebooks. You can edit this metadata by
activating the menu `View -> Cell Toolbar -> Edit Metadata`.
