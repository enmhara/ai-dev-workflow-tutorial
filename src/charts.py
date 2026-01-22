"""Plotly chart generation functions for the Sales Dashboard."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_sales_trend_chart(df: pd.DataFrame) -> go.Figure:
    """Create interactive line chart showing sales over time.

    Args:
        df: DataFrame with columns ['date', 'total_amount'].

    Returns:
        Plotly Figure object with sales trend line chart.
    """
    fig = px.line(
        df,
        x="date",
        y="total_amount",
        title="Sales Trend Over Time",
        labels={"date": "Date", "total_amount": "Sales Amount"},
    )
    fig.update_traces(hovertemplate="Date: %{x}<br>Sales: $%{y:,.2f}<extra></extra>")
    fig.update_layout(yaxis_tickprefix="$", yaxis_tickformat=",")
    return fig


def create_category_chart(df: pd.DataFrame) -> go.Figure:
    """Create interactive bar chart showing sales by category.

    Args:
        df: DataFrame with columns ['category', 'total_amount'].

    Returns:
        Plotly Figure object with category bar chart.
    """
    fig = px.bar(
        df,
        x="category",
        y="total_amount",
        title="Sales by Category",
        labels={"category": "Category", "total_amount": "Sales Amount"},
    )
    fig.update_traces(
        hovertemplate="Category: %{x}<br>Sales: $%{y:,.2f}<extra></extra>"
    )
    fig.update_layout(yaxis_tickprefix="$", yaxis_tickformat=",")
    return fig


def create_region_chart(df: pd.DataFrame) -> go.Figure:
    """Create interactive bar chart showing sales by region.

    Args:
        df: DataFrame with columns ['region', 'total_amount'].

    Returns:
        Plotly Figure object with region bar chart.
    """
    fig = px.bar(
        df,
        x="region",
        y="total_amount",
        title="Sales by Region",
        labels={"region": "Region", "total_amount": "Sales Amount"},
    )
    fig.update_traces(hovertemplate="Region: %{x}<br>Sales: $%{y:,.2f}<extra></extra>")
    fig.update_layout(yaxis_tickprefix="$", yaxis_tickformat=",")
    return fig
