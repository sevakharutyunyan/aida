"""

LAT (load-adapt-transform) ~ human way of

"""


class __Estimator:

    __IO = {
        "Ridge": {
            "engine": Ridge,
            "params": dict(alpha=0.1)
        },
        "Logit": {
            "engine": LogisticRegression,
            "params": dict(random_state=0)
        }

    }

    def __init__(self, *, method: str):
        self._method = method

    @property
    def engine(self):
        return self.__IO[self._method]["engine"]

    @property
    def params(self):
        return self.__IO[self._method]["params"]

    def __call__(self, *args, **kwargs):
        return self.engine(**self.params)