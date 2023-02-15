from .utils import preprocess_text

def prepare_description(df):
    df["description"] = df["description"].fillna("")
    df["text"] = df["product"] + " " + df["description"]
    df["text"] = df["text"].apply(preprocess_text)
    return df
