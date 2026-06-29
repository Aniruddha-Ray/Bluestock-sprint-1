import re

def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace(r"[()]", "", regex=True)
    )

    return df

def normalize_year(year):

    if year is None:
        return None

    year = str(year)

    match = re.search(r"(20\d{2})", year)

    if match:
        return int(match.group())

    return None


def normalize_ticker(ticker):

    if ticker is None:
        return None

    ticker = str(ticker).upper()

    ticker = ticker.replace(".NS", "")

    ticker = ticker.replace(" EQ", "")

    ticker = ticker.strip()

    return ticker