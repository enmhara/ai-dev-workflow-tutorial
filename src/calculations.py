"""KPI calculations and data aggregations for the Sales Dashboard."""

import pandas as pd


def calculate_total_sales(df: pd.DataFrame) -> float:
    """Calculate total sales amount from transaction data.

    Args:
        df: DataFrame with 'total_amount' column.

    Returns:
        Sum of all transaction amounts.
    """
    return df["total_amount"].sum()


def calculate_total_orders(df: pd.DataFrame) -> int:
    """Calculate count of unique orders.

    Args:
        df: DataFrame with 'order_id' column.

    Returns:
        Count of unique order IDs.
    """
    return df["order_id"].nunique()


def aggregate_sales_by_date(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales by date for trend analysis.

    Args:
        df: DataFrame with 'date' and 'total_amount' columns.

    Returns:
        DataFrame with columns ['date', 'total_amount'], sorted by date ascending.
    """
    return df.groupby("date")["total_amount"].sum().reset_index().sort_values("date")


def aggregate_sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales by product category.

    Args:
        df: DataFrame with 'category' and 'total_amount' columns.

    Returns:
        DataFrame with columns ['category', 'total_amount'], sorted by total_amount descending.
    """
    return (
        df.groupby("category", observed=True)["total_amount"]
        .sum()
        .reset_index()
        .sort_values("total_amount", ascending=False)
    )


def aggregate_sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales by geographic region.

    Args:
        df: DataFrame with 'region' and 'total_amount' columns.

    Returns:
        DataFrame with columns ['region', 'total_amount'], sorted by total_amount descending.
    """
    return (
        df.groupby("region", observed=True)["total_amount"]
        .sum()
        .reset_index()
        .sort_values("total_amount", ascending=False)
    )
