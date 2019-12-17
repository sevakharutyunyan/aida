import pathlib

import pandas as pd


class LocalLoader:

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
            "reader": "",
            "writer": ""
        }
    }

    def __init__(self, path: str):
        self.path = path
        self.__load()

    def __load(self):
        self.__get_extension()
        self.__read()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, other: str):
        new_path = pathlib.Path(other)
        if not new_path.is_file():
            raise FileExistsError(f"{other} is not a valid path.")
        self._path = new_path

    def __get_extension(self):
        for extension in self.__EXTENSIONS:
            if self.path.name.endswith(extension):
                self.__extension = extension
                break
        else:
            self.__extension = None

    def __read(self):
        reader = self.__IO.get(self.__extension)["reader"]
        params = self.__IO.get(self.__extension)["params"]
        self.data = reader(self.path, **params)


class RemoteLoader:
    pass
