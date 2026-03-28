# Medical Insurance Cost Analysis

Professional regression analysis project for understanding and predicting medical insurance charges using demographic and lifestyle factors.

## Executive Summary

This project combines exploratory data analysis and supervised machine learning to identify the strongest cost drivers in medical insurance pricing and evaluate predictive model performance.

## Project Objectives

- analyze how age, BMI, smoking status, region, and number of children relate to insurance charges
- build baseline and regularized regression models
- compare model performance and refine predictive quality
- produce reproducible visual and modeling artifacts

## Tech Stack

- Python
- pandas and numpy
- matplotlib and seaborn
- scikit-learn
- Jupyter Notebook

## Repository Structure

```text
medical-insurance-analysis/
  data/
    README.md
    raw/
      README.md
      insurance.csv
  notebooks/
    README.md
    insurance_analysis.ipynb
  reports/
    README.md
    figures/
      README.md
      Age vs Charges.png
      Bmi vs Charges.png
      Comparison of Regression Models.png
      Correlation Heatmap.png
      ...
  requirements.txt
  README.md
```

## Analysis Workflow

1. Load and clean raw insurance data.
2. Perform exploratory analysis with univariate and bivariate visuals.
3. Train and compare regression models.
4. Review model metrics and select/refine best-performing approach.

## Models Evaluated

- Simple Linear Regression
- Multiple Linear Regression
- Ridge Regression
- Polynomial Ridge Regression

## Key Insight Areas

- smoking status influence on insurance charges
- BMI and age relationship with cost
- contribution of region and dependents to charge variation
- model trade-offs between bias and variance

## Setup and Run

From the `medical-insurance-analysis` folder:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/insurance_analysis.ipynb
```

## Artifacts

- source dataset: `data/raw/insurance.csv`
- notebook analysis: `notebooks/insurance_analysis.ipynb`
- exported visuals: `reports/figures`

## Author

Visura Rodrigo
