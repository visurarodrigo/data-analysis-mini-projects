# Movie Ratings Explorer

SQL + Python exploratory analysis project based on the IMDb Top 1000 movies dataset.

## Project Overview

This project demonstrates a practical analytics workflow inside Jupyter:

- load a CSV dataset with pandas
- persist records into SQLite
- query the database using ipython-sql
- visualize rating and genre patterns with Python charts

## Repository Structure

```text
Movie-Ratings-Explorer-/
  data/
    raw/
      imdb_top_1000.csv
    processed/
      movies.db
  notebooks/
    movie_ratings_explorer.ipynb
  reports/
    figures/
      Average IMDb Rating by Release Year ( Since 1970 ).png
      Distribution of IMDB Ratings.png
      Top 10 movie Genres by Count.png
  requirements.txt
  README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/movie_ratings_explorer.ipynb
```

## Analysis Scope

The notebook covers:

- highest-rated movie exploration
- genre frequency and ranking
- average ratings and trends by release year
- director-level and revenue-related SQL summaries

## Data and Database Paths

Notebook paths were standardized for portability:

- dataset: ../data/raw/imdb_top_1000.csv
- sqlite database: ../data/processed/movies.db

## Professional Improvements Applied

- moved data, notebook, and figures into a consistent analytics layout
- centralized generated visuals under reports/figures
- added explicit dependency management via requirements.txt
- cleaned and standardized project documentation

## Author

Visura Rodrigo
