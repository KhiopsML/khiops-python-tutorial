import argparse
import json


def main(args):
    # Process the input notebooks
    for input_nb_path in args.input_nb_paths:
        # Load the notebook and eliminate the cell metadata
        # except for the key "is_khiops_tutorial_solution"
        with open(input_nb_path) as input_nb_file:
            nb = json.load(input_nb_file)

        # Clean the notebook's general metadata
        nb_was_modified = False
        if "metadata" in nb:
            nb_metadata = nb["metadata"]
            if (
                "kernelspec" in nb_metadata
                and "display_name" in nb_metadata["kernelspec"]
                and nb_metadata["kernelspec"]["display_name"] != "Python 3"
            ):
                nb_metadata["kernelspec"]["display_name"] = "Python 3"
                nb_was_modified = True
            if "language_info" in nb_metadata:
                language_info = nb_metadata["language_info"]
                if "version" in language_info:
                    del language_info["version"]
                    nb_was_modified = True

        cells = nb["cells"]
        for cell in cells:
            # Clean outputs
            if cell["cell_type"] == "code":
                if len(cell["outputs"]) > 0:
                    cell["outputs"] = []
                    nb_was_modified = True
                if cell["execution_count"] is not None:
                    cell["execution_count"] = None
                    nb_was_modified = True

            # Clean metadata
            metadata = cell["metadata"]
            for key in list(metadata.keys()):
                if key != "is_khiops_tutorial_solution":
                    nb_was_modified = True
                    del metadata[key]
        # If modified: Write the clean notebook to the ouput
        if nb_was_modified:
            with open(input_nb_path, "w") as output_nb_file:
                output_nb_file.write(json.dumps(nb, indent=1))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog="my-nb-clean",
        description="Cleans the cell metadata excepting 'is_khiops_tutorial_solution'",
    )
    arg_parser.add_argument(
        "input_nb_paths", metavar="NB", nargs="+", help="Input notebook paths"
    )
    args = arg_parser.parse_args()
    main(args)
