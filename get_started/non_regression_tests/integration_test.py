import argparse
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError
from subprocess import run
import sys 


# /!\ Environnement variables of the files have to be added in the execution environnement

# list of files to run (notebook or script)
# launch it this way for example:
# python3 integration_tests/integreation_tests.py -lpath *path/to/notebook.ipynb* --cleanup *path/to/cleaning/script.py*
# -> it runs the notebooks and clean it after
parser = argparse.ArgumentParser()
parser.add_argument(
    "--list_path_to_run",
    "-lpath",
    action="extend",
    type=str,
    default=[],
    nargs="+",
    help="list of notebooks or scripts to run",
)
parser.add_argument(
    "--timeout",
    "-t",
    type=int,
    default=300,
    help="timeout of the execution",
)
parser.add_argument(
    "--cleanup",
    "-c",
    action="extend",
    type=str,
    default=[],
    nargs="+",
    help="list of cleanup scripts to run",
)

args = parser.parse_args()

list_path_to_run = args.list_path_to_run
# possible to change the timeout if the notebook is supposed to run longer
timeout = args.timeout
cleanup = args.cleanup

try:
    for file_to_run in list_path_to_run:
        print(f"Running {file_to_run}")
        # for the scripts
        if file_to_run.endswith(".py"):
            run([sys.executable, file_to_run], check=True)

        elif file_to_run.endswith(".ipynb"):
            # for the notebooks
            with open(file_to_run) as file:
                nb = nbformat.read(file, as_version=4)

            ep = ExecutePreprocessor(timeout=timeout, kernel_name="python3")

            try:
                out = ep.preprocess(
                    nb,
                    {
                        "metadata": {
                            # path of the notebook folder
                            "path": f"{'/'.join(file_to_run.split('/')[0:-1])}/"
                        }
                    },
                )

            except CellExecutionError:
                out = None
                msg = 'Error executing the notebook "%s".\n\n' % f"{file_to_run}"
                print(msg)
                raise
except Exception as e:
    msg = f"Error executing the file {file_to_run}: you should check the logs."
    print(msg)
    raise
finally:
    print("Start cleanup")
    for file_to_run in cleanup:
        print(f"Running {file_to_run}")
        run([sys.executable, file_to_run])