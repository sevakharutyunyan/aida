from aida.panel.cross_sectional.loader import LocalLoader


class Adapter:

    __slots__ = ['n_rows', 'n_cols', '__data', 'n', 'm']

    def __init__(self, path):
        self.__data = LocalLoader(path).data
        if self.__data.empty:
            raise ValueError('Data do not exist!')

    @property
    def m(self):
        """Alias for number of observations"""
        return self.__data.shape[0]

    @property
    def n(self):
        """Alias for number of columns"""
        return self.__data.shape[-1]

    @property
    def n_rows(self):
        return self.__data.shape[0]

    @property
    def n_cols(self):
        return self.__data.shape[-1]


if __name__ == "__main__":
    adapter = Adapter(r'/home/sevak/Downloads/clinical_data.tsv')
    print(adapter.n_cols)
