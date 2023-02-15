from typing import Protocol

class BaseSearchEngine(Protocol):
    def __init__(self, *args, **kwargs):
        self.name = None

    def fit(self, X, *args, **kwargs):
        ...

    def predict(self, request, X_transformed, top_n, *args, **kwargs):
        ...
