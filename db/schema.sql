CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    ticker TEXT UNIQUE NOT NULL,
    company_name TEXT NOT NULL,
    sector_id INTEGER
);

CREATE TABLE profitandloss (
    company_id INTEGER,
    year INTEGER,
    sales REAL,
    operating_profit REAL,
    net_profit REAL,

    PRIMARY KEY (company_id, year),

    FOREIGN KEY(company_id)
    REFERENCES companies(company_id)
);

CREATE TABLE balancesheet (

    company_id INTEGER,

    year INTEGER,

    total_assets REAL,

    total_liabilities REAL,

    shareholders_equity REAL,

    PRIMARY KEY(company_id, year),

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id)

);

CREATE TABLE cashflow (

    company_id INTEGER,

    year INTEGER,

    operating_cashflow REAL,

    investing_cashflow REAL,

    financing_cashflow REAL,

    PRIMARY KEY(company_id, year),

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id)

);

CREATE TABLE analysis (

    company_id INTEGER PRIMARY KEY,

    analysis TEXT,

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id)

);

CREATE TABLE documents (

    company_id INTEGER PRIMARY KEY,

    annual_report TEXT,

    concall_notes TEXT,

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id)

);

CREATE TABLE prosandcons (

    company_id INTEGER PRIMARY KEY,

    pros TEXT,

    cons TEXT,

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id)

);

CREATE TABLE sectors (

    sector_id INTEGER PRIMARY KEY,

    sector_name TEXT

);

CREATE TABLE stock_prices (

    company_id INTEGER,

    trade_date DATE,

    open REAL,

    high REAL,

    low REAL,

    close REAL,

    volume INTEGER,

    PRIMARY KEY(company_id, trade_date),

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id)

);

CREATE TABLE financial_ratios (

    company_id INTEGER,

    year INTEGER,

    roe REAL,

    roce REAL,

    pe REAL,

    pb REAL,

    debt_equity REAL,

    PRIMARY KEY(company_id, year),

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id)

);

CREATE TABLE peer_groups (

    company_id INTEGER,

    peer_company_id INTEGER,

    PRIMARY KEY(company_id, peer_company_id),

    FOREIGN KEY(company_id)

    REFERENCES companies(company_id),

    FOREIGN KEY(peer_company_id)

    REFERENCES companies(company_id)

);

import sqlite3

connection = sqlite3.connect("db/nifty100.db")

connection.execute("PRAGMA foreign_keys = ON;")

with open("db/schema.sql", "r") as f:

    connection.executescript(f.read())

connection.commit()

connection.close()

print("Database Created Successfully")

