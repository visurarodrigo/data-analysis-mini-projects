from pathlib import Path
import sys

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.preprocess import clean_data, feature_engineering, load_data


DATA_PATH = BASE_DIR / "data" / "raw" / "netflix_titles.csv"
MAP_PATH = BASE_DIR / "notebooks" / "images" / "netflix_map.html"


def build_dataset() -> pd.DataFrame:
    """Load and preprocess dashboard source data."""
    data = load_data(DATA_PATH)
    data = clean_data(data)
    data = feature_engineering(data)
    return data


def build_genres_figure(data: pd.DataFrame):
    top_genres = (
        data["primary_genre"].value_counts().head(10).sort_values().reset_index()
    )
    top_genres.columns = ["Genre", "Count"]

    if top_genres.empty:
        fig = px.bar(title="Top 10 Genres")
        fig.add_annotation(
            text="No genre data available",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            font={"size": 16},
        )
        fig.update_layout(height=420, margin=dict(l=20, r=20, t=60, b=20))
        return fig

    fig = px.bar(
        top_genres,
        x="Count",
        y="Genre",
        orientation="h",
        title="Top 10 Genres",
        color="Count",
        color_continuous_scale="Tealgrn",
    )
    fig.update_layout(
        height=420,
        margin=dict(l=20, r=20, t=60, b=20),
        coloraxis_showscale=False,
        template="plotly_white",
    )
    return fig


def build_yearly_figure(data: pd.DataFrame):
    yearly = data["year_added"].dropna().astype(int).value_counts().sort_index().reset_index()
    yearly.columns = ["Year", "Count"]

    if yearly.empty:
        fig = px.line(title="Content Added Over Time")
        fig.add_annotation(
            text="No timeline data available",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
            font={"size": 16},
        )
        fig.update_layout(height=420, margin=dict(l=20, r=20, t=60, b=20))
        return fig

    fig = px.line(
        yearly,
        x="Year",
        y="Count",
        markers=True,
        title="Content Added Over Time",
    )
    fig.update_traces(line_color="#1f8a70", marker_color="#1f8a70")
    fig.update_layout(height=420, margin=dict(l=20, r=20, t=60, b=20), template="plotly_white")
    return fig


def load_map_html() -> str:
    """Return embedded map HTML if available, else a fallback message."""
    if MAP_PATH.exists():
        return MAP_PATH.read_text(encoding="utf-8")
    return """
    <html><body style='font-family:Segoe UI, sans-serif; padding:24px;'>
      <h3>Map Not Found</h3>
      <p>Please generate <code>notebooks/images/netflix_map.html</code> by running
      <code>notebooks/03_interactive_visuals.ipynb</code>.</p>
    </body></html>
    """


df = build_dataset()
fig_genres = build_genres_figure(df)
fig_years = build_yearly_figure(df)
map_html = load_map_html()

app = dash.Dash(__name__)
app.title = "Netflix Media Consumption Dashboard"

app.layout = html.Main(
    className="page-shell",
    children=[
        html.Section(
            className="hero",
            children=[
                html.P("Interactive Analytics", className="eyebrow"),
                html.H1("Netflix Media Consumption Dashboard"),
                html.P(
                    "Genre popularity, content growth over time, and global distribution in one view.",
                    className="subtitle",
                ),
            ],
        ),
        html.Section(
            className="grid-two",
            children=[
                html.Article(
                    className="card",
                    children=[
                        html.H2("Top Genres"),
                        dcc.Graph(
                            figure=fig_genres,
                            config={"displayModeBar": False, "responsive": True},
                            className="chart",
                        ),
                    ],
                ),
                html.Article(
                    className="card",
                    children=[
                        html.H2("Content Added Over Time"),
                        dcc.Graph(
                            figure=fig_years,
                            config={"displayModeBar": False, "responsive": True},
                            className="chart",
                        ),
                    ],
                ),
            ],
        ),
        html.Section(
            className="card card-map",
            children=[
                html.H2("Geographic Distribution"),
                html.Iframe(srcDoc=map_html, className="map-frame", title="Netflix Geographic Distribution"),
            ],
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)