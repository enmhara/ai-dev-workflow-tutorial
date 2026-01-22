# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a tutorial repository for teaching AI-assisted development workflows. It guides students through building a Streamlit sales dashboard using Cursor, Claude Code, GitHub, Jira, and spec-kit. The focus is on the **process** (spec-driven development, traceability, professional workflows) rather than the code itself.

## Project Structure

- `docs/` - Tutorial documentation (numbered 00-08 for reading order)
- `prd/ecommerce-analytics.md` - Product Requirements Document for the dashboard project
- `data/sales-data.csv` - Sample e-commerce transaction data (~1000 records)

## The Tutorial Workflow

Students follow this workflow:
1. PRD → spec-kit → Jira tasks → Code → Commit → Push → Deploy to Streamlit Community Cloud

Key conventions:
- Jira project key: `ECOM`
- Commit messages must include Jira issue key: `ECOM-1: description`
- All code changes should be traceable back to Jira issues

## Tech Stack for Dashboard Project

- Python 3.11+
- Streamlit (web framework)
- Plotly (interactive charts)
- Pandas (data processing)
- uv (package manager)
- spec-kit (requirements-to-solution workflow)

## Dashboard Requirements

The tutorial builds a sales dashboard with:
- 2 KPI scorecards (Total Sales, Total Orders)
- 1 line chart (sales trend over time)
- 2 bar charts (sales by category, sales by region)

Data source: `data/sales-data.csv` with columns: date, order_id, product, category, region, quantity, unit_price, total_amount

## Active Technologies
- Python 3.11+ + Streamlit (web framework), Plotly (interactive charts), Pandas (data processing) (001-sales-dashboard)
- Static CSV file (`data/sales-data.csv`) (001-sales-dashboard)

## Recent Changes
- 001-sales-dashboard: Added Python 3.11+ + Streamlit (web framework), Plotly (interactive charts), Pandas (data processing)
