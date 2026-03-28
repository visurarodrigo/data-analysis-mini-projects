# Reports Directory

## Overview

This directory stores generated analysis artifacts including visualizations, summary tables, and insights documentation.

## Subdirectories

- **`figures/`**: Exported chart images (PNG, SVG formats)

## Artifact Organization

### Visualizations

All charts exported from the notebook are saved in `figures/`:

| Chart | Type | Use Case |
|-------|------|----------|
| `top_genres_distribution.png` | Bar chart | Genre frequency distribution |
| `rating_distribution.png` | Histogram | Rating spread across dataset |
| `rating_trend_over_time.png` | Line chart | Temporal trends in average ratings |

### File Naming Convention

Use descriptive names with underscores:
```
chart_descriptor_[optional_context].png
```

Example:
- ✓ `genre_distribution_top10.png`
- ✓ `rating_trend_1975_2024.png`
- ✓ `director_productivity.png`

### Regenerating Artifacts

All visualizations are reproducible by running the notebook:

```bash
jupyter notebook notebooks/movie_ratings_explorer.ipynb
```

After execution, charts are displayed inline. To save them:

```python
plt.savefig('reports/figures/chart_name.png', dpi=300, bbox_inches='tight')
```

### Export Settings

**Recommended chart export parameters**:
- **DPI**: 300 (high quality for reports/presentations)
- **Format**: PNG (universal compatibility)
- **Bounding box**: 'tight' (removes white borders)

Example:
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12, 6))
# ... plot code ...
plt.savefig('reports/figures/chart_name.png', dpi=300, bbox_inches='tight')
```

### Quality Checklist

Before sharing charts:
- [ ] Chart title is clear and descriptive
- [ ] Axes are labeled with units
- [ ] Color palette is colorblind-friendly (Husl, tab10)
- [ ] Legend is included (if applicable)
- [ ] Export DPI is 300+ for printing
- [ ] File naming follows convention

## Summary Documents

Additional analysis summaries can be added here:
- Executive summaries (`.md` or `.docx`)
- Detailed findings reports (`.pdf`)
- Statistical tables (`.csv` or `.xlsx`)

## Access & Sharing

Figures are ready for:
- ✓ Portfolio/GitHub README display
- ✓ Presentation slides and reports
- ✓ Blog posts and documentation
- ✓ Print media (300 DPI)
