# Raw Data

## Dataset: IMDb Top 1000 Movies

### File: `imdb_top_1000.csv`

**Source**: IMDb public dataset  
**Format**: Comma-separated values (CSV)  
**Size**: ~500 KB  
**Encoding**: UTF-8  
**Records**: 1,000 movies  

### Schema

| Column | Type | Description |
|--------|------|-------------|
| Series_Title | Text | Movie title |
| Released_Year | Integer | Year of release |
| Genre | Text | Pipe-separated genre tags (e.g., "Drama\|Crime\|Thriller") |
| Director | Text | Director name(s) |
| IMDB_Rating | Float | IMDb user rating (0.0–10.0) |
| No_of_Votes | Integer | Total votes cast by IMDb users |
| Gross | Float | Box office revenue (USD, may contain NULLs) |
| Meta_score | Float | Metacritic score (may contain NULLs) |

### Data Quality Notes

- **Missing Values**: Some records lack `Gross` or `Meta_score` (handled by NOT NULL checks in SQL queries)
- **Immutability**: This file should never be modified after import to maintain reproducibility
- **Encoding**: Uses UTF-8 with BOM signature (handled by `encoding='utf-8-sig'` in pandas)

### Usage

Load into pandas:
```python
from pathlib import Path
df = pd.read_csv(Path('../data/raw/imdb_top_1000.csv'), encoding='utf-8-sig')
```

Or import directly to SQLite:
```bash
sqlite3 ../data/processed/movies.db
.mode csv
.import imdb_top_1000.csv Movies
```

### Regeneration

To obtain a fresh copy:
1. Download from official IMDb dataset source
2. Place in this directory as `imdb_top_1000.csv`
3. Re-run the notebook to regenerate the SQLite database
