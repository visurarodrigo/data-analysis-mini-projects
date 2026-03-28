# Figures Directory

## Overview

This directory stores all exported visualization charts generated during the exploratory analysis phase.

## Chart Inventory

### 1. Top Genres Distribution (`top_genres_distribution.png`)
- **Type**: Horizontal bar chart
- **Data**: Top 10 movie genres by count
- **Insight**: Drama leads with ~155 films; Action, Crime, Thriller follow
- **Generated from**: Query 2 (Step 4, SQL Analysis)

### 2. Rating Distribution (`rating_distribution.png`)
- **Type**: Histogram with KDE curve
- **Data**: All 1,000 movies' IMDb ratings
- **Insight**: Ratings concentrate between 7.0–8.5; mean ≈ 7.82
- **Generated from**: Visualization 2 (Step 5, Python Analysis)

### 3. Rating Trend Over Time (`rating_trend_over_time.png`)
- **Type**: Line chart with polynomial trend
- **Data**: Average IMDb rating by release year (1975–present)
- **Insight**: No clear trend; ratings fluctuate around 7.8 with slight upward/downward movement
- **Generated from**: Visualization 3 (Step 5, Python Analysis)

## Regenerating Figures

All figures are 100% reproducible by re-running the notebook:

```bash
cd Movie-Ratings-Explorer-
jupyter notebook notebooks/movie_ratings_explorer.ipynb
```

**Steps**:
1. Execute cells sequentially (Shift+Enter)
2. Charts render in notebook output cells
3. Optionally export using `plt.savefig()`:

```python
plt.savefig('reports/figures/chart_name.png', dpi=300, bbox_inches='tight')
```

## Chart Specifications

| Property | Value |
|----------|-------|
| Resolution | 300 DPI (print-quality) |
| Format | PNG (lossless) |
| Color Palette | Seaborn Husl/default (colorblind-safe) |
| Font | System default (Arial-like) |
| Figure Size | 12×6 inches (1200×600 default) |

## Usage Examples

### In Markdown (README, blogs)
```markdown
![Genre Distribution](reports/figures/top_genres_distribution.png)
```

### In PowerPoint/Google Slides
1. Insert → Image
2. Select from `reports/figures/`
3. Resize as needed

### In LaTeX/PDF Reports
```latex
\includegraphics[width=0.8\textwidth]{reports/figures/rating_trend_over_time.png}
```

## File Naming Convention

New figures should follow this pattern:
```
[metric]_[chart_type]_[optional_qualifier].png
```

Examples:
- `rating_histogram_density.png`
- `director_barplot_top20.png`
- `revenue_scatter_by_genre.png`

## Quality Assurance

Before sharing figures:
- [ ] Chart includes clear title
- [ ] Axes labeled with descriptions
- [ ] Units displayed (if applicable)
- [ ] Legend included (if multi-series)
- [ ] No overlapping text or truncated labels
- [ ] Colors are distinct and accessible
- [ ] Resolution is 300 DPI for printing
- [ ] File follows naming convention

## Future Enhancements

Consider generating:
- Interactive visualizations (Plotly)
- Dashboard with filters
- Heatmaps for correlation analysis
- Network diagrams for director relationships
