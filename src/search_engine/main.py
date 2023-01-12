from search_engine.data import preprocessing
from search_engine.models.interface import BaseSearchEngine


def search_products(request, X, top_n, search_engine: BaseSearchEngine):
    # prepare data
    X = _prepare_data(X)
    # fit-predict
    X_transformed = search_engine.fit(X=X.text).toarray()
    return search_engine.predict(request, X_transformed, top_n)


def _prepare_data(X):
    return preprocessing.prepare_description(X)
