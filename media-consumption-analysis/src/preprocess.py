from pathlib import Path
from typing import Union

import pandas as pd


PathLike = Union[str, Path]


def load_data(path: PathLike) -> pd.DataFrame:
    """Load source data into a pandas DataFrame.

    Args:
        path: Path to the CSV file.

    Returns:
        Loaded DataFrame.
    """
    return pd.read_csv(Path(path), encoding="utf-8-sig")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize the raw Netflix dataset.

    This function preserves notebook compatibility while making preprocessing
    behavior more explicit and safer.
    """
    cleaned = df.copy()

    # Standardize column names once to snake_case style.
    cleaned.columns = [c.strip().lower().replace(" ", "_") for c in cleaned.columns]

    # Remove exact duplicate rows.
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    # Normalize text columns by trimming surrounding whitespace.
    text_cols = cleaned.select_dtypes(include=["object"]).columns
    for col in text_cols:
        cleaned[col] = cleaned[col].astype(str).str.strip()

    if "release_year" in cleaned.columns:
        cleaned["release_year"] = pd.to_numeric(cleaned["release_year"], errors="coerce")

    if "date_added" in cleaned.columns:
        cleaned["date_added"] = pd.to_datetime(cleaned["date_added"], errors="coerce")

    # Fill missing categorical values with a consistent placeholder.
    categorical_cols = cleaned.select_dtypes(include=["object"]).columns
    cleaned[categorical_cols] = cleaned[categorical_cols].replace({"": pd.NA}).fillna("Unknown")

    return cleaned


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Create analysis-ready derived features used across notebooks and app."""
    features = df.copy()

    if "date_added" in features.columns:
        features["year_added"] = features["date_added"].dt.year
        features["month_added"] = features["date_added"].dt.month

    if "duration" in features.columns:
        duration = features["duration"].astype(str).str.extract(r"(?P<value>\d+)\s*(?P<unit>[A-Za-z]+)")
        features["duration_minutes"] = pd.to_numeric(duration["value"], errors="coerce")
        features["duration_type"] = duration["unit"].str.lower()
        features["duration_type"] = features["duration_type"].fillna("unknown")

    if "listed_in" in features.columns:
        features["primary_genre"] = (
            features["listed_in"].astype(str).str.split(",").str[0].str.strip().replace("", "Unknown")
        )

    return features