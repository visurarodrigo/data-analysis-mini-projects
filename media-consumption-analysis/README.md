# Media Consumption Analysis

Netflix media consumption analysis project with exploratory notebooks and an interactive Dash dashboard.

## Project Overview

This repository analyzes Netflix titles data to identify genre trends, content growth over time, and geographic distribution.
It includes:

- notebook-based data exploration and visual analytics
- reusable preprocessing logic in src
- an interactive dashboard built with Dash and Plotly

## Repository Structure

```text
media-consumption-analysis/
  app/
    assets/
      styles.css
    screenshot/
      dash app 1.jpg
      dash app 2.jpg
    dash_app.py
  data/
    raw/
      netflix_titles.csv
    worldcities.xlsx
  notebooks/
    data/
      country_coords.json
    images/
      Content Added to Netflix Over Time.jpg
      Distribution of Content Types.png
      Distribution of Ratings.png
      Interactive map Countries producing Netflix content.jpg
      netflix_map.html
      Top 10 Genres on Netflix (Interactive).jpg
      Top 10 Genres on Netflix.png
      WordCloud of Genres.png
    01_load_clean_explore.ipynb
    02_exploratory_analysis.ipynb
    03_interactive_visuals.ipynb
  src/
    preprocess.py
  requirements.txt
  README.md
```

## Key Analyses

- top genres and category frequency
- yearly trend of content added to Netflix
- country-level production distribution
- visual storytelling with static and interactive charts

## Dashboard

The Dash app displays:

- Top Genres (bar chart)
- Content Added Over Time (line chart)
- Geographic Distribution (embedded interactive map)

## Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run notebooks or launch dashboard.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app/dash_app.py
```

Open http://127.0.0.1:8050 in your browser.

## Notebook Workflow

Run notebooks in order for a reproducible analysis path:

1. notebooks/01_load_clean_explore.ipynb
2. notebooks/02_exploratory_analysis.ipynb
3. notebooks/03_interactive_visuals.ipynb

## Professional Improvements Applied

- removed unresolved merge conflict content from documentation
- updated dashboard paths to be repository-relative (portable across machines)
- completed dependency specification in requirements.txt
- standardized README structure for maintainability

## Author

Visura Rodrigo
