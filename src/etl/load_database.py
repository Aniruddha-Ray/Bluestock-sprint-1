import sqlite3
import pandas as pd

from loader import load_excel

conn = sqlite3.connect("db/nifty100.db")

conn.execute("PRAGMA foreign_keys=ON")

audit = []

def load_table(file_path, table_name):

    df = load_excel(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    audit.append({
        "table": table_name,
        "rows_loaded": len(df),
        "rejected_rows": 0
    })

    print(f"{table_name} Loaded ({len(df)} rows)")

    load_table("data/raw/companies.xlsx","companies")

load_table("data/raw/profitandloss.xlsx","profitandloss")

load_table("data/raw/balancesheet.xlsx","balancesheet")

load_table("data/raw/cashflow.xlsx","cashflow")

load_table("data/raw/analysis.xlsx","analysis")

load_table("data/raw/documents.xlsx","documents")

load_table("data/raw/prosandcons.xlsx","prosandcons")

load_table("data/raw/sectors.xlsx","sectors")

load_table("data/raw/stock_prices.xlsx","stock_prices")

load_table("data/raw/financial_ratios.xlsx","financial_ratios")

load_table("data/raw/peer_groups.xlsx","peer_groups")


pd.DataFrame(audit).to_csv(
    "output/load_audit.csv",
    index=False
)

conn.commit()

conn.close()

print("Loading Finished")

