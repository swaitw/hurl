import glob
import importlib
import os

from flask import Flask

app = Flask(__name__)


def load_tests():
    for python_file in glob.glob("tests_*/**/*.py", recursive=True):
        module_name = python_file.split(".")[0].replace(os.path.sep, ".")
        print("loading %s" % module_name)
        try:
            importlib.import_module(module_name)
        except ImportError as err:
            print("Error:", err)


@app.after_request
def remove_header(response):
    response.headers["Server"] = "Flask Server"
    return response
