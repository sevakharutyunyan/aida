"""
Panel package has solutions for 2 types of data.

1. Cross-Sectional
2. Time-Series

"""

import pathlib

import pandas as pd


class __Loader:

    __slots__ = ["data", "_path", "__extension"]

    __EXTENSIONS = {"csv", "tsv", "xlsx"}

    __IO = {
        "csv": {
            "reader": pd.read_csv,
            "writer": "",
        },
        "tsv": {
            "reader": pd.read_csv,
            "params": {
              "delimiter": "\t"
            },
            "writer": "",
        },
        "excel": {
            "reader": pd.read_excel,
            "writer": None
        }
    }

    def __init__(self, path: str, local=True):
        self.path = path
        if local:
            self.__local_load()
        if not local:
            raise NotImplementedError

    def __local_load(self):
        self.__get_extension()
        self.__read()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, other: str):
        if other.startswith("https"):
            self._path = other
        else:
            new_path = pathlib.Path(other)
            if not new_path.is_file():
                raise FileExistsError(f"{other} is not a valid path.")
            self._path = new_path

    def __get_extension(self):
        # TODO: heavily relies on naming convection.
        for extension in self.__EXTENSIONS:
            if self.path.endswith(extension):
                self.__extension = extension
                break
        else:
            self.__extension = None

    def __read(self):
        reader = self.__IO.get(self.__extension)["reader"]
        params = self.__IO.get(self.__extension)["params"]
        self.data = reader(self.path, **params)