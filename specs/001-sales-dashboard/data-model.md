# Data Model: E-Commerce Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-22
**Source**: Feature specification entities + CSV schema analysis

## Entities

### Transaction

The atomic unit of sales data. Each row in `data/sales-data.csv` represents one transaction.

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| `date` | date | Transaction date | Required, valid date format (YYYY-MM-DD) |
| `order_id` | string | Unique order identifier | Required, format: ORD-XXXXXX |
| `product` | string | Product name | Required, non-empty |
| `category` | string | Product category | Required, one of valid categories |
| `region` | string | Geographic region | Required, one of valid regions |
| `quantity` | integer | Units purchased | Required, positive integer |
| `unit_price` | decimal | Price per unit | Required, positive decimal |
| `total_amount` | decimal | Transaction total | Required, equals quantity * unit_price |

**Source**: `data/sales-data.csv`
**Record Count**: ~1000 transactions
**Date Range**: 12 months of historical data

### Product Category (Enumeration)

Fixed set of product classifications for segment analysis.

| Value | Description |
|-------|-------------|
| `Electronics` | Electronic devices and gadgets |
| `Accessories` | Product accessories and add-ons |
| `Audio` | Audio equipment and accessories |
| `Wearables` | Wearable technology devices |
| `Smart Home` | Smart home devices and systems |

**Usage**: Filtering and grouping for category breakdown chart

### Region (Enumeration)

Fixed set of geographic territories for territorial analysis.

| Value | Description |
|-------|-------------|
| `North` | Northern territory |
| `South` | Southern territory |
| `East` | Eastern territory |
| `West` | Western territory |

**Usage**: Filtering and grouping for region breakdown chart

### KPI (Derived)

Calculated metrics derived from Transaction aggregations.

| Metric | Calculation | Format |
|--------|-------------|--------|
| `Total Sales` | `SUM(total_amount)` | Currency: $X,XXX,XXX.XX |
| `Total Orders` | `COUNT(DISTINCT order_id)` | Integer: X,XXX |

**Note**: KPIs are computed at runtime, not stored.

## Relationships

```
Transaction
    ├── belongs_to → Category (many-to-one)
    └── belongs_to → Region (many-to-one)

KPI
    └── derived_from → Transaction (aggregation)
```

## Data Flow

```
┌─────────────────────┐
│  sales-data.csv     │
│  (source of truth)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  data_loader.py     │
│  - Load CSV         │
│  - Validate schema  │
│  - Parse dates      │
│  - Cache with       │
│    @st.cache_data   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  DataFrame          │
│  (pandas)           │
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐ ┌─────────┐
│ calcs   │ │ charts  │
│ .py     │ │ .py     │
└────┬────┘ └────┬────┘
     │           │
     ▼           ▼
┌─────────┐ ┌─────────┐
│  KPIs   │ │ Plotly  │
│         │ │ Figures │
└─────────┘ └─────────┘
```

## Pandas DataFrame Schema

After loading and parsing, the DataFrame has the following dtypes:

```python
{
    'date': 'datetime64[ns]',
    'order_id': 'object',      # string
    'product': 'object',       # string
    'category': 'category',    # categorical for efficiency
    'region': 'category',      # categorical for efficiency
    'quantity': 'int64',
    'unit_price': 'float64',
    'total_amount': 'float64'
}
```

## Aggregation Queries

### Total Sales KPI
```python
df['total_amount'].sum()
```

### Total Orders KPI
```python
df['order_id'].nunique()
```

### Sales by Date (Trend Chart)
```python
df.groupby('date')['total_amount'].sum().reset_index()
```

### Sales by Category
```python
df.groupby('category')['total_amount'].sum().sort_values(ascending=False).reset_index()
```

### Sales by Region
```python
df.groupby('region')['total_amount'].sum().sort_values(ascending=False).reset_index()
```

## Validation Rules

### On Load
1. File exists at `data/sales-data.csv`
2. Required columns present: `date`, `order_id`, `product`, `category`, `region`, `quantity`, `unit_price`, `total_amount`
3. No completely empty file

### Per Record (Graceful Handling)
1. Date parseable as valid date
2. Numeric fields (`quantity`, `unit_price`, `total_amount`) are valid numbers
3. Category is one of the 5 valid values
4. Region is one of the 4 valid values

**Handling Invalid Records**: Skip and continue processing valid records. Log warning if significant number of records skipped.
