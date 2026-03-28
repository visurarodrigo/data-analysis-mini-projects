# Movie Ratings Explorer

**A Comprehensive Analysis of IMDb's Top 1000 Movies**

## Executive Summary

This project explores the IMDb Top 1000 movies dataset using SQL queries and Python visualizations. The analysis combines relational database techniques (SQLite) with exploratory data analysis to uncover patterns in movie ratings, genre distributions, director productivity, and revenue trends. The workflow demonstrates a production-ready approach to data ingestion, querying, and insight generation within a Jupyter notebook environment.

---

## Objectives

1. **Data Ingestion & Storage**: Load IMDb data from CSV and persist records in SQLite for efficient querying
2. **SQL-Based Analysis**: Execute targeted queries to identify top-rated films, genre patterns, and director performance
3. **Trend Analysis**: Visualize rating distributions and temporal trends over 50 years of cinema
4. **Insight Generation**: Generate actionable insights about movie success factors (ratings, genres, directors, revenue)

---

## Technology Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Primary analysis language |
| **Pandas** | Data loading, manipulation, and SQL queries |
| **SQLite** | Relational database for structured queries |
| **ipython-sql** | SQL magic commands in Jupyter |
| **Matplotlib / Seaborn** | Professional data visualization |
| **NumPy** | Statistical computations and trend analysis |

---

## Repository Structure

```
Movie-Ratings-Explorer-/
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── data/
│   ├── raw/
│   │   └── imdb_top_1000.csv          # Source dataset (immutable)
│   └── processed/
│       └── movies.db                   # SQLite database (generated)
├── notebooks/
│   └── movie_ratings_explorer.ipynb    # Primary analysis notebook
└── reports/
    └── figures/                        # Exported visualizations
        ├── top_genres_distribution.png
        ├── rating_distribution.png
        └── rating_trend_over_time.png
```

---

## Analytical Workflow

### Step 1: Environment Setup
Install required packages and configure Jupyter SQL magic extension for interactive database querying.

### Step 2: Data Ingestion & SQLite Setup
- Load IMDb CSV dataset (1000 records) into pandas DataFrame
- Create SQLite database with optimized schema
- Import cleaned records into Movies table

### Step 3: SQL-Based Exploratory Analysis
Execute 6 targeted queries:
1. **Top-rated films**: Identify highest IMDb ratings
2. **Genre distribution**: Count movies by genre
3. **Recent acclaim**: Filter films post-2010 with ratings > 8.0
4. **Prolific directors**: Rank directors by movie count
5. **Genre performance**: Calculate average ratings and revenue by genre
6. **Director quality**: Identify highest-rated directors (min. 5 films)

### Step 4: Python Visualizations
Generate 3 professional charts:
- **Bar chart**: Top 10 genres by movie count
- **Histogram**: Distribution of IMDb ratings with KDE curve
- **Line chart**: 50-year trend in average ratings with polynomial fit

---

## Key Insights

- **Rating Distribution**: Top 1000 movies cluster around 7.0–8.0 IMDb rating, skewed toward excellence
- **Genre Leaders**: Drama dominates the dataset; Action, Crime, and Thriller follow
- **Temporal Trend**: Average ratings fluctuate over decades; modern films show slight quality variation
- **Director Consistency**: Directors with 5+ films in the dataset maintain 7.5+ average ratings

---

## Setup & Execution

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Jupyter or JupyterLab

### Installation

```bash
# Clone or navigate to project directory
cd Movie-Ratings-Explorer-

# Create virtual environment
python -m venv .venv

# Activate environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Notebook

```bash
# Launch Jupyter
jupyter notebook

# Open: notebooks/movie_ratings_explorer.ipynb
# Execute cells sequentially (Shift+Enter)
```

**Note**: The notebook will automatically:
- Create the SQLite database in `data/processed/`
- Generate visualizations inline
- Display SQL query results in formatted tables

---

## Project Artifacts

| Artifact | Description |
|----------|-------------|
| `movies.db` | SQLite database (900 KB) with Movies table and indexes |
| `top_genres_distribution.png` | Bar chart of genre frequencies |
| `rating_distribution.png` | Histogram with KDE overlay |
| `rating_trend_over_time.png` | Time-series trend with polynomial fit |

---

## Future Enhancements

- **Predictive Modeling**: Build regression model to predict movie ratings from features (genre, year, director)
- **Advanced Visualizations**: Interactive Plotly dashboards for filter-able exploration
- **Text Analysis**: Parse director names and genre tags for network analysis
- **Time Series Forecasting**: Forecast future movie quality trends

---

## Author

**Visura Rodrigo**
