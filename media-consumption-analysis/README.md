# Media Consumption Analysis

Professional data analysis project exploring Netflix catalog patterns through notebook-based EDA and an interactive Dash dashboard.

## Executive Summary

This repository analyzes Netflix titles to uncover content composition trends, genre popularity, release behavior, and geographic distribution. The project combines:

- structured preprocessing utilities for reusable data preparation
- staged exploratory notebooks for transparent analysis workflow
- an interactive dashboard for presentation and quick insight consumption

## Project Objectives

- profile Netflix content mix by type, genre, and rating
- evaluate content additions over time
- visualize country-level production presence
- provide both analysis artifacts and an interactive app for stakeholders

## Tech Stack

- Python
- pandas
- matplotlib and seaborn
- plotly and dash
- folium
- Jupyter Notebook

## Repository Structure

```text
media-consumption-analysis/
  app/
    README.md
    dash_app.py
    assets/
      README.md
      styles.css
    screenshot/
      README.md
      dash app 1.jpg
      dash app 2.jpg
  data/
    README.md
    raw/
      README.md
      netflix_titles.csv
    worldcities.xlsx
  notebooks/
    README.md
    01_load_clean_explore.ipynb
    02_exploratory_analysis.ipynb
    03_interactive_visuals.ipynb
    data/
      README.md
      country_coords.json
    images/
      README.md
      Content Added to Netflix Over Time.jpg
      Distribution of Content Types.png
      Distribution of Ratings.png
      Interactive map Countries producing Netflix content.jpg
      netflix_map.html
      Top 10 Genres on Netflix (Interactive).jpg
      Top 10 Genres on Netflix.png
      WordCloud of Genres.png
  src/
    README.md
    preprocess.py
  requirements.txt
  README.md
```

## Analysis Workflow

Run notebooks in this sequence for a reproducible pipeline:

1. notebooks/01_load_clean_explore.ipynb
2. notebooks/02_exploratory_analysis.ipynb
3. notebooks/03_interactive_visuals.ipynb

## Dashboard Features

The Dash app presents:

- Top 10 Genres (interactive bar chart)
- Content Added Over Time (interactive line chart)
- Geographic Distribution (embedded Folium map)

## Setup and Run

From the media-consumption-analysis project folder:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app/dash_app.py
```

Open http://127.0.0.1:8050 in your browser.

## Output Artifacts

- notebook-generated visual outputs are stored in notebooks/images
- dashboard preview screenshots are stored in app/screenshot

## Author

Visura Rodrigo
