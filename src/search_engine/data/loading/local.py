import pandas as pd
from search_engine.config import settings


def load_data():
    return pd.read_excel(settings.ROOT_DIR / "data/products.xlsx")
