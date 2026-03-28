# Notebooks Directory

## Primary Notebook: `movie_ratings_explorer.ipynb`

### Purpose

This Jupyter notebook contains the complete analytical workflow for exploring the IMDb Top 1000 movies dataset. It combines SQL queries with Python visualizations to generate insights about movie ratings, genre distributions, director performance, and temporal trends.

### Notebook Structure

| Step | Section | Outputs |
|------|---------|---------|
| 1 | Environment Setup | Installed packages, imported libraries |
| 2 | Data Ingestion & SQLite Setup | Created `movies.db` with 1,000 records |
| 3 | SQL Magic Connection | Enabled interactive SQL querying |
| 4 | Exploratory SQL Analysis | 6 formatted query result tables |
| 5 | Python Visualizations | 3 professional matplotlib charts |

### Execution Guide

**Prerequisites**:
- Python 3.10+
- Dependencies installed (`pip install -r requirements.txt`)
- Jupyter kernel available

**Running the notebook**:
1. Launch Jupyter: `jupyter notebook`
2. Navigate to `notebooks/movie_ratings_explorer.ipynb`
3. Execute cells sequentially using **Shift+Enter**
4. Review outputs in notebook cells

**Execution time**: ~2–3 minutes (includes SQL queries and visualization rendering)

### Key Outputs

- **Database**: `../data/processed/movies.db` (900 KB SQLite file)
- **Query Results**: 6 formatted tables with SQL insights (displayed inline)
- **Visualizations**: 3 matplotlib charts (bar, histogram, line chart)

### Reproducibility

The notebook is fully reproducible:
- All file paths use portable `Path()` patterns (work on Windows/macOS/Linux)
- Random seeds set for consistent visualization styling
- SQL queries are deterministic (no randomization)
- Chart styling uses Seaborn theme for consistency

### Optional: Save Visualizations

To export charts as PNG files:
```python
import matplotlib.pyplot as plt
plt.savefig('../reports/figures/chart_name.png', dpi=300, bbox_inches='tight')
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| "ModuleNotFoundError: No module named 'pandas'" | Run `pip install -r requirements.txt` |
| Database connection fails | Verify `../data/processed/` directory exists |
| SQL queries return no results | Ensure Step 2 (data import) completed successfully |
| Charts not displaying | Restart kernel and re-run notebook |

### Version Control

- Notebook file is tracked in Git
- Output cells are cleared before commits (best practice)
- Data files in `data/processed/` are typically added to `.gitignore`
