
import pandas as pd

from aida.panel.__init__ import __Loader


class Adapter:

    __Loader = __Loader

    def __init__(self, path):
        self.__data = self.__Loader(path, local=True).data
        if self.__data.empty:
            raise ValueError('Data do not exist!')

    @property
    def n_rows(self):
        return self.__data.shape[0]

    @property
    def n_cols(self):
        return self.__data.shape[-1]
