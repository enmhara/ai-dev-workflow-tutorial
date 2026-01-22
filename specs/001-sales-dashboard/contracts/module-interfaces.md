# Module Interface Contracts: E-Commerce Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-22
**Purpose**: Define function signatures and expected behavior for each module

## Overview

Since this is a Streamlit application (not a REST API), contracts are defined as module interfaces specifying function signatures, input/output types, and behavior expectations.

---

## Module: `src/data_loader.py`

### `load_sales_data() -> pd.DataFrame`

Loads and validates sales data from CSV file.

**Returns**: `pandas.DataFrame` with validated sales data

**Raises**:
- `FileNotFoundError`: If `data/sales-data.csv` does not exist
- `ValueError`: If required columns are missing

**Behavior**:
- Uses `@st.cache_data` decorator for caching
- Parses `date` column as datetime
- Converts `category` and `region` to categorical dtype
- Drops rows with missing required values (graceful handling)

**Example**:
```python
df = load_sales_data()
# Returns DataFrame with columns:
# date, order_id, product, category, region, quantity, unit_price, total_amount
```

---

## Module: `src/calculations.py`

### `calculate_total_sales(df: pd.DataFrame) -> float`

Calculates total sales amount from transaction data.

**Parameters**:
- `df`: DataFrame with `total_amount` column

**Returns**: `float` - Sum of all transaction amounts

**Example**:
```python
total = calculate_total_sales(df)
# Returns: 672450.75 (example value)
```

---

### `calculate_total_orders(df: pd.DataFrame) -> int`

Calculates count of unique orders.

**Parameters**:
- `df`: DataFrame with `order_id` column

**Returns**: `int` - Count of unique order IDs

**Example**:
```python
orders = calculate_total_orders(df)
# Returns: 482
```

---

### `aggregate_sales_by_date(df: pd.DataFrame) -> pd.DataFrame`

Aggregates sales by date for trend analysis.

**Parameters**:
- `df`: DataFrame with `date` and `total_amount` columns

**Returns**: `pd.DataFrame` with columns `['date', 'total_amount']`, sorted by date ascending

**Example**:
```python
trend_df = aggregate_sales_by_date(df)
# Returns:
#         date  total_amount
# 0 2024-01-03       1234.56
# 1 2024-01-04       2345.67
# ...
```

---

### `aggregate_sales_by_category(df: pd.DataFrame) -> pd.DataFrame`

Aggregates sales by product category.

**Parameters**:
- `df`: DataFrame with `category` and `total_amount` columns

**Returns**: `pd.DataFrame` with columns `['category', 'total_amount']`, sorted by total_amount descending

**Example**:
```python
category_df = aggregate_sales_by_category(df)
# Returns:
#       category  total_amount
# 0  Electronics      250000.00
# 1        Audio      150000.00
# ...
```

---

### `aggregate_sales_by_region(df: pd.DataFrame) -> pd.DataFrame`

Aggregates sales by geographic region.

**Parameters**:
- `df`: DataFrame with `region` and `total_amount` columns

**Returns**: `pd.DataFrame` with columns `['region', 'total_amount']`, sorted by total_amount descending

**Example**:
```python
region_df = aggregate_sales_by_region(df)
# Returns:
#   region  total_amount
# 0  North      200000.00
# 1   East      180000.00
# ...
```

---

## Module: `src/charts.py`

### `create_sales_trend_chart(df: pd.DataFrame) -> plotly.graph_objects.Figure`

Creates interactive line chart showing sales over time.

**Parameters**:
- `df`: DataFrame with columns `['date', 'total_amount']` (output of `aggregate_sales_by_date`)

**Returns**: Plotly Figure object

**Requirements**:
- X-axis: Date with appropriate formatting
- Y-axis: Sales amount with currency formatting
- Interactive tooltips showing exact date and value
- Clear title and axis labels

**Example**:
```python
fig = create_sales_trend_chart(trend_df)
st.plotly_chart(fig, use_container_width=True)
```

---

### `create_category_chart(df: pd.DataFrame) -> plotly.graph_objects.Figure`

Creates interactive bar chart showing sales by category.

**Parameters**:
- `df`: DataFrame with columns `['category', 'total_amount']` (output of `aggregate_sales_by_category`)

**Returns**: Plotly Figure object

**Requirements**:
- Bars sorted by value (highest to lowest)
- Interactive tooltips showing category and exact value
- Currency formatting on values
- All 5 categories visible
- Clear title and axis labels

**Example**:
```python
fig = create_category_chart(category_df)
st.plotly_chart(fig, use_container_width=True)
```

---

### `create_region_chart(df: pd.DataFrame) -> plotly.graph_objects.Figure`

Creates interactive bar chart showing sales by region.

**Parameters**:
- `df`: DataFrame with columns `['region', 'total_amount']` (output of `aggregate_sales_by_region`)

**Returns**: Plotly Figure object

**Requirements**:
- Bars sorted by value (highest to lowest)
- Interactive tooltips showing region and exact value
- Currency formatting on values
- All 4 regions visible
- Clear title and axis labels

**Example**:
```python
fig = create_region_chart(region_df)
st.plotly_chart(fig, use_container_width=True)
```

---

## Main Application: `app.py`

### Application Flow

```python
# 1. Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# 2. Load data (cached)
try:
    df = load_sales_data()
except FileNotFoundError:
    st.error("Unable to load sales data. Please contact support.")
    st.stop()

# 3. Display header
st.title("E-Commerce Sales Dashboard")

# 4. Display KPIs
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Sales", f"${calculate_total_sales(df):,.2f}")
with col2:
    st.metric("Total Orders", f"{calculate_total_orders(df):,}")

# 5. Display trend chart
st.subheader("Sales Trend")
st.plotly_chart(create_sales_trend_chart(aggregate_sales_by_date(df)))

# 6. Display category and region charts
col1, col2 = st.columns(2)
with col1:
    st.subheader("Sales by Category")
    st.plotly_chart(create_category_chart(aggregate_sales_by_category(df)))
with col2:
    st.subheader("Sales by Region")
    st.plotly_chart(create_region_chart(aggregate_sales_by_region(df)))
```

---

## Type Definitions

For reference, here are the expected DataFrame schemas:

### Raw Sales Data
```python
SalesDataFrame = DataFrame[{
    'date': datetime64[ns],
    'order_id': str,
    'product': str,
    'category': Literal['Electronics', 'Accessories', 'Audio', 'Wearables', 'Smart Home'],
    'region': Literal['North', 'South', 'East', 'West'],
    'quantity': int,
    'unit_price': float,
    'total_amount': float
}]
```

### Aggregated DataFrames
```python
TrendDataFrame = DataFrame[{'date': datetime64[ns], 'total_amount': float}]
CategoryDataFrame = DataFrame[{'category': str, 'total_amount': float}]
RegionDataFrame = DataFrame[{'region': str, 'total_amount': float}]
```
