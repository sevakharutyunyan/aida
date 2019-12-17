from aida.panel.cross_sectional.adapter import Adapter


class Transformer:

    def __init__(self, pre_process=False):
        self.data = Adapter.__data

    def drop_cols_with_miss_vals(self, percent: [int, float] = 80):
        self.data = self.data.dropna(axis=1, how='all')
