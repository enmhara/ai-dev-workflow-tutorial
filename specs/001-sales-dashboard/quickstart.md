# Quickstart Guide: E-Commerce Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-22
**Purpose**: Get the development environment running quickly

## Prerequisites

- Python 3.11 or higher
- `uv` package manager installed ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- Git

## Setup Steps

### 1. Clone and Navigate

```bash
cd ai-dev-workflow-tutorial
git checkout 001-sales-dashboard
```

### 2. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Verify Data File

Ensure `data/sales-data.csv` exists:

```bash
ls data/sales-data.csv
head -5 data/sales-data.csv
```

### 5. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

## Development Workflow

### Running Locally

```bash
# Start development server with auto-reload
streamlit run app.py

# The app automatically reloads when you save changes
```

### Code Linting

```bash
# Install ruff (if not already)
uv pip install ruff

# Run linter
ruff check src/ app.py

# Auto-fix issues
ruff check --fix src/ app.py
```

### Project Structure

```
.
├── app.py                 # Main Streamlit entry point
├── src/
│   ├── __init__.py
│   ├── data_loader.py     # CSV loading and validation
│   ├── calculations.py    # KPI calculations
│   └── charts.py          # Plotly chart generation
├── data/
│   └── sales-data.csv     # Source data
└── requirements.txt       # Pinned dependencies
```

## Expected Dependencies

`requirements.txt`:
```
streamlit>=1.31.0
plotly>=5.18.0
pandas>=2.1.0
```

## Verification Checklist

After running the app, verify:

- [ ] Dashboard loads without errors
- [ ] Total Sales KPI displays (expected: ~$650,000-$700,000)
- [ ] Total Orders KPI displays (expected: 482)
- [ ] Sales Trend line chart is visible and interactive
- [ ] Sales by Category bar chart shows all 5 categories
- [ ] Sales by Region bar chart shows all 4 regions
- [ ] Hovering over charts shows tooltips with exact values

## Common Issues

### "ModuleNotFoundError: No module named 'src'"

Make sure you're running from the repository root:
```bash
cd /path/to/ai-dev-workflow-tutorial
streamlit run app.py
```

### "FileNotFoundError: data/sales-data.csv"

Verify the data file exists:
```bash
ls -la data/
```

### Port 8501 already in use

Kill existing Streamlit processes or use a different port:
```bash
streamlit run app.py --server.port 8502
```

## Deployment

### Streamlit Community Cloud

1. Push changes to `main` branch
2. Connect repository to Streamlit Community Cloud
3. App deploys automatically

Required files for deployment:
- `app.py` at repository root
- `requirements.txt` with pinned versions
- `data/sales-data.csv` committed to repository

## Commit Convention

All commits must include the Jira issue key:

```bash
git commit -m "ECOM-1: Add KPI scorecards"
git commit -m "ECOM-2: Implement sales trend chart"
```
