# Medical Insurance Analysis

End-to-end regression analysis project for predicting medical insurance charges and identifying major cost drivers.

## Project Summary

This project analyzes insurance cost data using exploratory data analysis and supervised regression models.
The notebook covers:

- data preparation and cleaning
- exploratory analysis and visual diagnostics
- baseline and advanced regression models
- model comparison and refinement

## Repository Structure

```text
medical-insurance-analysis/
  data/
    raw/
      insurance.csv
  notebooks/
    insurance_analysis.ipynb
  reports/
    figures/
      Age vs Charges.png
      Bmi vs Charges.png
      Comparison of Regression Models.png
      Correlation Heatmap.png
      ...
  requirements.txt
  README.md
```

## Tech Stack

- Python 3.10+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- jupyter

## Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the notebook.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/insurance_analysis.ipynb
```

## Modeling Scope

Models evaluated in the notebook include:

- simple linear regression
- multiple linear regression
- ridge regression
- polynomial ridge regression

## Key Insight Areas

- impact of smoking status on charges
- relationship between BMI and charges
- age-based cost patterns
- relative effect of region and number of children

## Notes

- Figures produced during EDA and model evaluation are stored under reports/figures.
- Dataset used in this project is stored under data/raw.

## Author

Visura Rodrigo
