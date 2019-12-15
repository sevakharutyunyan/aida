from aida.panel.cross_sectional.loader import LocalLoader


class Adapter:

    def __init__(self, path):
        self.data = LocalLoader(path).data


if __name__ == "__main__":
    adapter = Adapter(r'/home/sevak/Downloads/clinical_data.tsv')
    print(adapter.data)
