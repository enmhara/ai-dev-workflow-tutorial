"""Data loading and validation for the E-Commerce Sales Dashboard."""

import pandas as pd
import streamlit as st

REQUIRED_COLUMNS = [
    "date",
    "order_id",
    "product",
    "category",
    "region",
    "quantity",
    "unit_price",
    "total_amount",
]

DATA_PATH = "data/sales-data.csv"


@st.cache_data
def load_sales_data() -> pd.DataFrame:
    """Load and validate sales data from CSV file.

    Returns:
        pd.DataFrame: Validated sales data with parsed dates and categorical columns.

    Raises:
        FileNotFoundError: If the data file does not exist.
        ValueError: If required columns are missing.
    """
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["category"] = df["category"].astype("category")
    df["region"] = df["region"].astype("category")

    df = df.dropna(subset=["date", "total_amount"])

    return df
