import pandas as pd

from .normaliser import (
    normalize_columns,
)

def load_excel(path):

    df = pd.read_excel(path)

    df = normalize_columns(df)

    return df


if __name__ == "__main__":

    df = load_excel("data/raw/company.xlsx")

    df = df.fillna("")

    print(df.head())

    print(df.columns)