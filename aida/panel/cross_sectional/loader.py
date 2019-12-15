import pathlib

import pandas as pd


class LocalLoader:

    __EXTENSIONS = {"csv", "tsv", "xlsx"}

    def __init__(self, path: str):
        self.path = path
        self.load()

    def load(self):
        self.__get_extension()
        self.__read()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, other):
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
        if self.__extension == "csv":
            self.data = pd.read_csv(self.path)
        if self.__extension == "tsv":
            self.data = pd.read_csv(self.path, delimiter="\t")
        if self.__extension == "xlsx":
            self.data == pd.read_excel(self.path)


class RemoteLoader:
    pass


if __name__ == "__main__":
    loader = LocalLoader(r'/home/sevak/Downloads/clinical_data.tsv')
    print(loader.data)
