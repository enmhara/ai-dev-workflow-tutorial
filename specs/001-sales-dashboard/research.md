# Research: E-Commerce Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-22
**Purpose**: Resolve technical decisions and best practices for implementation

## Research Topics

### 1. Streamlit Application Structure

**Decision**: Use `app.py` at repository root with `src/` module for business logic

**Rationale**:
- Streamlit Community Cloud expects `app.py` or similar at repository root by default
- Separating business logic into `src/` modules follows Constitution Principle I (code simplicity)
- Clean separation enables easier testing and maintenance

**Alternatives Considered**:
- Single monolithic `app.py`: Rejected because it violates single-purpose function principle
- `src/app.py` with package structure: Rejected because it complicates Streamlit Cloud deployment

### 2. Plotly Chart Types for Dashboard

**Decision**: Use `plotly.express` for all charts

**Rationale**:
- `plotly.express` provides high-level API with sensible defaults
- Built-in interactive tooltips satisfy FR-008
- Simpler code than `plotly.graph_objects` while meeting all requirements
- Easy sorting and formatting options

**Chart Mapping**:
| Requirement | Chart Type | Plotly Function |
|-------------|------------|-----------------|
| Sales trend over time | Line chart | `px.line()` |
| Sales by category | Bar chart | `px.bar()` |
| Sales by region | Bar chart | `px.bar()` |

**Alternatives Considered**:
- `plotly.graph_objects`: More control but more verbose; unnecessary for this use case
- Altair: Good library but Plotly specified in constitution
- Matplotlib: Not interactive; violates FR-008

### 3. KPI Display Pattern in Streamlit

**Decision**: Use `st.metric()` for KPI scorecards

**Rationale**:
- Native Streamlit component designed for KPIs
- Built-in formatting support for currency and numbers
- Professional appearance suitable for executive presentations (FR-010)
- Supports delta indicators if future enhancement needed

**Alternatives Considered**:
- Custom HTML/CSS: More flexible but harder to maintain; violates simplicity principle
- `st.write()` with formatting: Less visually prominent; doesn't meet "prominent display" requirement

### 4. Data Loading Strategy

**Decision**: Load CSV once at app start using `@st.cache_data` decorator

**Rationale**:
- Caching prevents re-reading CSV on every interaction
- Meets performance goal (5 second load time)
- Standard Streamlit pattern for data loading
- Pandas `read_csv()` handles date parsing automatically

**Data Validation**:
- Check file exists before loading
- Validate required columns present
- Handle missing/malformed values gracefully (edge case from spec)

**Alternatives Considered**:
- No caching: Would cause poor performance on interactions
- Database storage: Over-engineering for ~1000 static records
- Session state: More complex; caching is sufficient

### 5. Currency Formatting

**Decision**: Use Python locale or f-string formatting for currency display

**Rationale**:
- `${:,.2f}` format string produces `$X,XXX,XXX.XX` format
- Consistent with FR-001 requirement
- Works with both Pandas and direct Python formatting

**Implementation**:
```python
# For KPI display
f"${total_sales:,.2f}"

# For chart tooltips (Plotly handles automatically with hovertemplate)
hovertemplate="$%{y:,.2f}"
```

### 6. Error Handling Strategy

**Decision**: Display user-friendly error messages using `st.error()`

**Rationale**:
- Meets edge case requirements from spec
- Non-technical users need clear guidance
- Prevents app crashes from displaying to end users

**Error Scenarios**:
| Scenario | User Message |
|----------|--------------|
| File missing | "Unable to load sales data. Please contact support." |
| Empty file | "No sales data available for the selected period." |
| Malformed data | Skip invalid records silently; show available data |

### 7. Layout and Responsiveness

**Decision**: Use Streamlit columns for layout organization

**Rationale**:
- `st.columns()` provides responsive grid layout
- KPIs can be displayed side-by-side
- Charts can be full-width for maximum visibility
- Works across different screen sizes

**Layout Plan**:
```
[Header/Title]
[KPI: Total Sales] [KPI: Total Orders]
[Sales Trend Chart - full width]
[Category Chart] [Region Chart]
```

### 8. Deployment Configuration

**Decision**: Use Streamlit Community Cloud with default configuration

**Rationale**:
- Free tier suitable for tutorial/demo purposes
- Automatic deployment from GitHub main branch
- No additional infrastructure needed
- Meets FR-011 (publicly accessible URL)

**Required Files**:
- `requirements.txt`: Pinned dependencies
- `.python-version` or `runtime.txt`: Python version specification

## Dependencies Resolution

### Production Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | >=1.31.0 | Web framework |
| plotly | >=5.18.0 | Interactive charts |
| pandas | >=2.1.0 | Data processing |

### Development Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| ruff | >=0.2.0 | Linting (Constitution Principle III) |

## Summary

All technical decisions align with:
- Constitution principles (simplicity, user-friendly visualizations, Python best practices, environment isolation)
- Functional requirements (FR-001 through FR-011)
- Success criteria (SC-001 through SC-010)
- Edge case handling requirements

No NEEDS CLARIFICATION items remain. Ready to proceed to Phase 1.
