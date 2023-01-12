def prepare_description(df):
    df["description"] = df["description"].fillna("")
    df["text"] = df["product"] + " " + df["description"]
    return df
