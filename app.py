"""E-Commerce Sales Dashboard - Main Streamlit Application."""

import streamlit as st

from src.calculations import (
    aggregate_sales_by_category,
    aggregate_sales_by_date,
    aggregate_sales_by_region,
    calculate_total_orders,
    calculate_total_sales,
)
from src.charts import create_category_chart, create_region_chart, create_sales_trend_chart
from src.data_loader import load_sales_data

st.set_page_config(page_title="Sales Dashboard", layout="wide")

try:
    df = load_sales_data()
except FileNotFoundError:
    st.error("Unable to load sales data. Please contact support.")
    st.stop()
except ValueError as e:
    st.error(f"Data validation error: {e}")
    st.stop()

st.title("E-Commerce Sales Dashboard")

# KPI Scorecards
kpi_col1, kpi_col2 = st.columns(2)
with kpi_col1:
    st.metric("Total Sales", f"${calculate_total_sales(df):,.2f}")
with kpi_col2:
    st.metric("Total Orders", f"{calculate_total_orders(df):,}")

# Sales Trend Chart
st.subheader("Sales Trend")
trend_data = aggregate_sales_by_date(df)
st.plotly_chart(create_sales_trend_chart(trend_data), use_container_width=True)

# Category and Region Charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Sales by Category")
    category_data = aggregate_sales_by_category(df)
    st.plotly_chart(create_category_chart(category_data), use_container_width=True)

with chart_col2:
    st.subheader("Sales by Region")
    region_data = aggregate_sales_by_region(df)
    st.plotly_chart(create_region_chart(region_data), use_container_width=True)
