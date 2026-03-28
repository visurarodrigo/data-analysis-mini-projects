# Data Analysis Mini Projects

**A Professional Portfolio of Practice Projects Demonstrating Data Analysis Concepts**

## Executive Summary

This repository is a curated collection of four independent data analysis projects, each designed to practice and showcase specific analytical concepts and technologies. From time-series analysis to interactive dashboards, SQL-based analytics to predictive modeling, these projects collectively demonstrate a comprehensive understanding of modern data science workflows.

All projects follow professional standards including:
- Clean folder hierarchies with organized data, notebooks, and artifacts
- Comprehensive README documentation at project and folder levels
- Reproducible workflows with explicit dependency management
- Portable code using relative paths and version-controlled environments
- Production-quality visualizations and interactive dashboards

---

## Projects Overview

### 1. 📊 [Movie Ratings Explorer](Movie-Ratings-Explorer-)
**Focus**: SQL-Based Analytics & Data Engineering

Explore IMDb's Top 1000 movies using a hybrid SQL + Python workflow. This project demonstrates:
- **SQLite database design** for efficient querying of structured data
- **SQL analytics** with 6 targeted queries revealing rating trends, director performance, and genre patterns
- **Python visualization** with matplotlib/seaborn for publication-quality charts
- **Jupyter best practices** with markdown organization and portable file paths

**Key Skills**: SQLite, SQL queries, pandas integration, data visualization, trend analysis

---

### 2. 🎬 [Media Consumption Analysis](media-consumption-analysis)
**Focus**: Interactive Dashboards & Full-Stack Analytics

Analyze Netflix content library with a comprehensive 3-notebook pipeline and interactive Dash web application.

**Components**:
- **Notebook 1**: Data loading, cleaning, and exploratory validation
- **Notebook 2**: In-depth exploratory analysis with distribution patterns and genre insights
- **Notebook 3**: Interactive Plotly visualizations and Folium geographic mapping
- **Dash App**: Production-grade dashboard with responsive design and CSS styling

**Key Skills**: Data preprocessing, pandas workflows, Plotly/Dash, Folium mapping, web UI design, module organization

---

### 3. 🏥 [Medical Insurance Analysis](medical-insurance-analysis)
**Focus**: Predictive Modeling & Statistical Analysis

Build and evaluate regression models to predict insurance charges and understand feature impact on pricing.

**Workflow**:
- Exploratory data analysis with distribution and correlation studies
- Feature engineering and preprocessing for modeling
- Multiple regression model evaluation (Linear, Ridge, Decision Trees, Random Forest)
- Feature importance analysis and key driver identification

**Key Skills**: Statistical analysis, regression modeling, feature engineering, model evaluation, scikit-learn

---

### 4. 📈 [Stock Price Analysis of Apple Inc]([-Stock-Price-Analysis-of-Apple-Inc])
**Focus**: Time-Series Analysis & Financial Analytics

Analyze Apple Inc. stock performance with focus on trends, volatility, and returns.

**Analysis Areas**:
- Historical price trends and moving averages
- Volatility measurement and interpretation
- Return calculations (daily, cumulative, annualized)
- Moving average convergence and momentum indicators

**Key Skills**: Time-series analysis, financial metrics, technical indicators, numpy/pandas operations

---

## Technology Stack Summary

| Category | Technologies |
|----------|---------------|
| **Languages** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy, SciPy |
| **Databases** | SQLite, SQL queries |
| **Visualization** | Matplotlib, Seaborn, Plotly, Folium |
| **ML/Modeling** | scikit-learn, statistical analysis |
| **Web Framework** | Plotly Dash |
| **Notebook Environment** | Jupyter, JupyterLab |
| **Package Management** | pip, virtual environments |

---

## Repository Structure

```
data-analysis-mini-projects/
├── README.md                              # This file
├── Movie-Ratings-Explorer-/
│   ├── README.md                          # Project documentation
│   ├── requirements.txt                   # Dependencies
│   ├── data/
│   │   ├── raw/                           # Source data
│   │   └── processed/                     # Generated database
│   ├── notebooks/
│   │   └── movie_ratings_explorer.ipynb
│   └── reports/
│       └── figures/                       # Exported visualizations
│
├── media-consumption-analysis/
│   ├── README.md                          # Project documentation
│   ├── requirements.txt                   # Dependencies
│   ├── app/                               # Dash web application
│   │   ├── dash_app.py
│   │   └── assets/
│   ├── data/
│   │   ├── raw/                           # Netflix dataset
│   │   └── processed/                     # Processed data
│   ├── notebooks/                         # 3-stage analysis pipeline
│   ├── src/
│   │   └── preprocess.py                  # Reusable preprocessing module
│   └── reports/
│
├── medical-insurance-analysis/
│   ├── README.md                          # Project documentation
│   ├── requirements.txt                   # Dependencies
│   ├── data/
│   │   └── raw/                           # Insurance dataset
│   ├── notebooks/
│   │   └── insurance_analysis.ipynb
│   └── reports/
│
└── -Stock-Price-Analysis-of-Apple-Inc/
    ├── README.md                          # Project documentation
    ├── requirements.txt                   # Dependencies
    ├── data/
    │   └── raw/                           # Historical stock data
    ├── notebooks/
    │   └── stock_change.ipynb
    └── reports/
        └── figures/                       # Generated charts
```

---

## Quick Start Guide

### Option 1: Run a Specific Project

```bash
# Example: Movie Ratings Explorer
cd Movie-Ratings-Explorer-

# Create virtual environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter and open the notebook
jupyter notebook notebooks/movie_ratings_explorer.ipynb
```

### Option 2: Run the Dash Dashboard (Media Consumption)

```bash
cd media-consumption-analysis

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Start the dashboard server
python app/dash_app.py

# Open browser to: http://127.0.0.1:8050/
```

### Option 3: Explore All Projects

1. Read each project's individual README for detailed setup instructions
2. Each project is self-contained with its own virtual environment
3. Start with simpler projects (Movie Ratings, Stock Analysis) before dashboards

---

## Key Features by Project

| Feature | Movie Ratings | Media Analysis | Insurance | Stock Analysis |
|---------|---------------|----------------|-----------|-----------------|
| Jupyter Notebook | ✅ | ✅ (3 notebooks) | ✅ | ✅ |
| SQL Analytics | ✅ | ❌ | ❌ | ❌ |
| Web Dashboard | ❌ | ✅ (Dash) | ❌ | ❌ |
| Geospatial Maps | ❌ | ✅ (Folium) | ❌ | ❌ |
| Predictive Models | ❌ | ❌ | ✅ | ❌ |
| Time Series | ❌ | ❌ | ❌ | ✅ |
| Visualization | ✅ | ✅ | ✅ | ✅ |

---

## Skills Demonstrated

### Data Engineering
- CSV data import and validation
- SQLite database design and queries
- Data pipelines from raw to processed assets
- Portable file path handling across environments

### Data Analysis
- Exploratory data analysis (EDA)
- Statistical distributions and correlations
- Trend identification and time-series decomposition
- Feature importance and driver analysis

### Machine Learning
- Regression modeling (Linear, Ridge, Tree-based)
- Feature engineering and preprocessing
- Model evaluation and cross-validation
- Hyperparameter tuning

### Visualization & Communication
- Publication-quality matplotlib/seaborn charts
- Interactive Plotly visualizations
- Web-based dashboards with Dash
- Geographic mapping with Folium
- Professional documentation and markdown

### Software Engineering
- Virtual environment management
- Dependency management with requirements.txt
- Modular code organization (preprocessing utilities)
- Portable project structures
- Professional README documentation

---

## Best Practices Applied

✅ **Reproducibility**: All projects use version-controlled environments and explicit dependencies

✅ **Portability**: Relative file paths work across Windows/macOS/Linux

✅ **Organization**: Consistent folder hierarchies (data → notebooks → reports)

✅ **Documentation**: Multi-level README files at project and folder levels

✅ **Quality**: Production-grade visualizations, styled code, professional commenting

✅ **Self-Contained**: Each project is independent with no cross-project dependencies

---

## How to Navigate

1. **Start Here**: Read this README to understand the portfolio scope
2. **Choose a Project**: Pick one based on your interest (see overview section above)
3. **Go Deeper**: Read the individual project README for detailed workflow
4. **Explore Code**: Open notebooks and examine the implementation
5. **Run It**: Follow setup instructions to execute the project locally

---

## Development Environment

All projects require:
- **Python 3.10+**
- **Virtual environment manager** (venv included in Python)
- **Jupyter** (installed via requirements.txt)
- **Optional**: JupyterLab for enhanced notebook editing

---

## Portfolio Expansion

This repository will be updated with additional practice projects as new concepts and techniques are explored. Each new project will follow the same professional standards and documentation patterns established here.

---

## Repository Standards

All projects in this portfolio follow:
- **Folder Structure**: Consistent data/notebooks/reports hierarchy
- **Naming**: Descriptive file names with underscores (not spaces)
- **Dependencies**: Explicit requirements.txt in each project
- **Documentation**: Comprehensive README at multiple levels
- **Reproducibility**: Portable paths, deterministic workflows
- **Code Quality**: Type hints, docstrings, error handling

---

## Author

**Visura Rodrigo**


