# Tasks: E-Commerce Sales Dashboard

**Input**: Design documents from `/specs/001-sales-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are NOT included as they were not explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `app.py` at repository root (Streamlit convention)
- Based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure: `src/` directory with `__init__.py`
- [x] T002 Create requirements.txt with pinned dependencies (streamlit>=1.31.0, plotly>=5.18.0, pandas>=2.1.0)
- [x] T003 [P] Create .python-version file specifying Python 3.11+
- [x] T004 [P] Verify data/sales-data.csv exists and validate column schema

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Implement `load_sales_data()` function with `@st.cache_data` decorator in src/data_loader.py
- [x] T006 Add CSV validation (check required columns, parse dates, handle missing values) in src/data_loader.py
- [x] T007 Add error handling for FileNotFoundError and ValueError in src/data_loader.py
- [x] T008 Create app.py with page configuration (`st.set_page_config(page_title="Sales Dashboard", layout="wide")`)
- [x] T009 Add data loading with error display (`st.error()` and `st.stop()`) in app.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - View Business Performance at a Glance (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders KPIs prominently so users can quickly assess overall business performance

**Independent Test**: Load the dashboard and verify that Total Sales (currency-formatted as $X,XXX,XXX.XX) and Total Orders (count as X,XXX) are prominently displayed at the top

### Implementation for User Story 1

- [x] T010 [P] [US1] Implement `calculate_total_sales(df)` function in src/calculations.py
- [x] T011 [P] [US1] Implement `calculate_total_orders(df)` function in src/calculations.py
- [x] T012 [US1] Add dashboard title and KPI section layout using `st.columns(2)` in app.py
- [x] T013 [US1] Display Total Sales KPI using `st.metric()` with currency formatting in app.py
- [x] T014 [US1] Display Total Orders KPI using `st.metric()` with number formatting in app.py

**Checkpoint**: User Story 1 complete - KPIs visible and correctly calculated (Total Sales ~$650,000-$700,000, Total Orders = 482)

---

## Phase 4: User Story 2 - Analyze Sales Trends Over Time (Priority: P2)

**Goal**: Show a visual representation of how sales have changed over time for strategic planning

**Independent Test**: Load the dashboard and interact with the trend chart - verify it shows sales over time with interactive tooltips displaying exact values for specific dates

### Implementation for User Story 2

- [x] T015 [P] [US2] Implement `aggregate_sales_by_date(df)` function in src/calculations.py
- [x] T016 [US2] Implement `create_sales_trend_chart(df)` function using `px.line()` in src/charts.py
- [x] T017 [US2] Add chart title, axis labels, and currency-formatted tooltips in src/charts.py
- [x] T018 [US2] Add Sales Trend section with subheader and chart display in app.py

**Checkpoint**: User Story 2 complete - Line chart shows sales trend over 12 months with interactive tooltips

---

## Phase 5: User Story 3 - Understand Sales by Product Category (Priority: P3)

**Goal**: Show sales broken down by product category for marketing budget allocation decisions

**Independent Test**: Load the dashboard and verify the category breakdown chart displays all 5 product categories (Electronics, Accessories, Audio, Wearables, Smart Home) sorted by sales value, with interactive tooltips

### Implementation for User Story 3

- [x] T019 [P] [US3] Implement `aggregate_sales_by_category(df)` function with descending sort in src/calculations.py
- [x] T020 [US3] Implement `create_category_chart(df)` function using `px.bar()` in src/charts.py
- [x] T021 [US3] Add chart title, axis labels, and currency-formatted tooltips in src/charts.py
- [x] T022 [US3] Add Sales by Category section in left column layout in app.py

**Checkpoint**: User Story 3 complete - Bar chart shows all 5 categories sorted highest to lowest with interactive tooltips

---

## Phase 6: User Story 4 - Understand Sales by Geographic Region (Priority: P4)

**Goal**: Show sales broken down by geographic region for territory management decisions

**Independent Test**: Load the dashboard and verify the region breakdown chart displays all 4 regions (North, South, East, West) sorted by sales value, with interactive tooltips

### Implementation for User Story 4

- [x] T023 [P] [US4] Implement `aggregate_sales_by_region(df)` function with descending sort in src/calculations.py
- [x] T024 [US4] Implement `create_region_chart(df)` function using `px.bar()` in src/charts.py
- [x] T025 [US4] Add chart title, axis labels, and currency-formatted tooltips in src/charts.py
- [x] T026 [US4] Add Sales by Region section in right column layout in app.py

**Checkpoint**: User Story 4 complete - Bar chart shows all 4 regions sorted highest to lowest with interactive tooltips

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and deployment preparation

- [x] T027 Verify all charts render within 2 seconds and dashboard loads within 5 seconds
- [x] T028 Run quickstart.md verification checklist in browser
- [x] T029 [P] Code cleanup: ensure PEP 8 compliance using ruff
- [x] T030 Verify deployment readiness (requirements.txt, .python-version, data file committed)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-6)**: All depend on Foundational phase completion
  - Can proceed in priority order (P1 → P2 → P3 → P4)
  - Or in parallel if team capacity allows
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational - No dependencies on US1 (uses same data loader)
- **User Story 3 (P3)**: Can start after Foundational - No dependencies on US1/US2
- **User Story 4 (P4)**: Can start after Foundational - No dependencies on US1/US2/US3

### Within Each User Story

- Calculation functions before chart functions
- Chart functions before app.py integration
- All src/ modules before app.py display code

### Parallel Opportunities

- T003, T004 can run in parallel (different files)
- T010, T011 can run in parallel (different functions, same file but independent)
- T015, T019, T023 can run in parallel (different aggregation functions)
- Once Foundational completes, all user stories can start in parallel

---

## Parallel Example: User Story 1

```bash
# Launch calculation functions in parallel:
Task: "Implement calculate_total_sales(df) function in src/calculations.py"
Task: "Implement calculate_total_orders(df) function in src/calculations.py"

# Then sequentially add app.py integration
```

## Parallel Example: All Aggregation Functions

```bash
# Once Foundational is complete, launch all aggregations in parallel:
Task: "Implement aggregate_sales_by_date(df) function in src/calculations.py"
Task: "Implement aggregate_sales_by_category(df) function in src/calculations.py"
Task: "Implement aggregate_sales_by_region(df) function in src/calculations.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Load dashboard, verify KPIs display correctly
5. Deploy to Streamlit Community Cloud for stakeholder review

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Test KPIs → Deploy (MVP!)
3. Add User Story 2 → Test trend chart → Deploy
4. Add User Story 3 → Test category chart → Deploy
5. Add User Story 4 → Test region chart → Deploy
6. Polish → Final deployment

### File Creation Order

1. `requirements.txt` - dependencies
2. `.python-version` - Python version
3. `src/__init__.py` - module initialization
4. `src/data_loader.py` - data loading
5. `src/calculations.py` - KPI and aggregation functions
6. `src/charts.py` - Plotly chart functions
7. `app.py` - main Streamlit application

---

## Notes

- [P] tasks = different files or independent functions, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group with format: `ECOM-X: description`
- Stop at any checkpoint to validate story independently
- All charts use `plotly.express` for simplicity per research.md decisions
