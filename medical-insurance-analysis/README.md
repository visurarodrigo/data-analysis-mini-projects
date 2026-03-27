# Medical Insurance Charges Analysis 💉📊

## 📋 Project Overview

This project provides a comprehensive analysis of medical insurance charges using advanced machine learning regression techniques. By analyzing demographic and health-related features of insured individuals, we develop predictive models to accurately estimate insurance costs and identify key cost-driving factors.

The analysis demonstrates professional data science practices including data preprocessing, exploratory data analysis (EDA), feature engineering, model development, and performance optimization. The project serves as an end-to-end example of regression modeling applied to real-world insurance data.

**Completed as part of:** IBM Data Analysis with Python (Coursera)

## 🎯 Objectives

- **Data Quality**: Clean and preprocess raw insurance data to handle missing values and inconsistencies
- **Exploratory Analysis**: Investigate patterns, distributions, and correlations in insurance charges
- **Model Development**: Build and compare multiple regression models with varying complexity
- **Optimization**: Refine models using regularization techniques and polynomial feature engineering
- **Business Insights**: Identify actionable factors that significantly impact insurance costs

## 📊 Dataset

**Source:** [IBM Cloud Object Storage](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/medical_insurance_dataset.csv)

**Size:** 1,338 records with 7 features

### Feature Description

| Feature          | Description                                          | Type        | Values/Range        |
|------------------|------------------------------------------------------|-------------|---------------------|
| `age`            | Age of the insured individual                        | Numerical   | 18-64 years         |
| `gender`         | Gender of the insured                                | Categorical | 1: Female, 2: Male  |
| `bmi`            | Body Mass Index (weight/height²)                     | Numerical   | 15.96-53.13         |
| `no_of_children` | Number of dependents covered by insurance            | Numerical   | 0-5                 |
| `smoker`         | Smoking status of the insured                        | Categorical | 1: Smoker, 2: Non-smoker |
| `region`         | Residential region in USA                            | Categorical | 1: NW, 2: NE, 3: SW, 4: SE |
| `charges`        | Individual medical insurance costs (USD)             | Numerical   | $1,121.87-$63,770.43 |

## 📁 Project Structure

```
medical-insurance-analysis/
│
├── insurance_analysis.ipynb    # Main Jupyter notebook with complete analysis
├── insurance.csv               # Dataset (downloaded automatically)
├── project.ipynb               # Additional project notebook
├── EDA/                        # Exploratory Data Analysis outputs
├── README.md                   # Project documentation (this file)
└── .gitignore                  # Git ignore file
```

## 🔬 Analysis Workflow

### 1. **Data Wrangling & Preprocessing**
   - Replace placeholder values (`?`) with NaN
   - Impute missing categorical features with mode (most frequent value)
   - Impute missing numerical features with mean
   - Convert data types and round charges for consistency
   - Validate data quality and check for remaining issues

### 2. **Exploratory Data Analysis (EDA)**
   - **Descriptive Statistics**: Summary statistics for numerical features
   - **Distribution Analysis**: Histograms, KDE plots, and box plots for outlier detection
   - **Categorical Analysis**: Count plots with frequency distributions
   - **Relationship Analysis**: Scatter plots (numerical) and box plots (categorical) vs charges
   - **Correlation Analysis**: Heatmap to identify linear relationships

### 3. **Model Development**
   
   #### Models Implemented:
   
   | Model                          | Description                                           | Key Features                    |
   |--------------------------------|-------------------------------------------------------|---------------------------------|
   | Simple Linear Regression       | Single predictor (BMI only)                           | Baseline performance            |
   | Multiple Linear Regression     | All features included                                 | Captures multi-feature patterns |
   | Ridge Regression (L2)          | Regularized linear regression (α=1.0)                 | Prevents overfitting            |
   | Polynomial Ridge Regression    | Polynomial features (degree=2) + regularization       | Captures non-linear relationships |

### 4. **Model Evaluation Metrics**
   - **MSE** (Mean Squared Error): Average squared prediction error
   - **RMSE** (Root Mean Squared Error): Standard deviation of residuals
   - **MAE** (Mean Absolute Error): Average absolute prediction error
   - **R² Score**: Proportion of variance explained by the model

### 5. **Model Refinement & Optimization**
   - **Hyperparameter Tuning**: Test multiple alpha values (0.001 to 1000) for Ridge regression
   - **Feature Engineering**: Create polynomial features to capture interaction effects
   - **Performance Comparison**: Visual and tabular comparison of all models

## 📈 Key Findings

### Primary Insights

1. **🚬 Smoking Status - Dominant Factor**
   - Strongest predictor of insurance charges
   - Smokers face significantly higher premiums (often 3-4x higher)
   - Categorical feature with the highest correlation to costs

2. **⚖️ BMI - Secondary Health Indicator**
   - Positive correlation with insurance charges
   - Higher BMI associated with increased health risks and costs
   - Interaction with smoking status amplifies impact

3. **👴 Age - Progressive Cost Factor**
   - Direct relationship: older individuals pay more
   - Reflects cumulative health risks over time
   - Steady increase across age ranges

4. **👨‍👩‍👧‍👦 Children & Region - Minimal Impact**
   - Number of children shows weak correlation
   - Regional differences exist but are relatively small
   - Gender shows no significant cost difference

### Model Performance Summary

| Model                    | RMSE          | MAE           | R² Score | Performance |
|--------------------------|---------------|---------------|----------|-------------|
| Simple LR (BMI)          | ~$11,500      | ~$9,000       | 0.039    | Poor        |
| Multiple LR              | ~$6,000       | ~$4,200       | 0.747    | Good        |
| Ridge Regression         | ~$6,000       | ~$4,200       | 0.747    | Good        |
| **Polynomial Ridge**     | **~$5,800**   | **~$4,000**   | **0.772**| **Best**    |

**Best Model:** Polynomial Ridge Regression (degree=2, α=1.0)  
**Improvement:** 5% error reduction and 3% R² increase over standard regression

## 🛠️ Technologies & Libraries

### Core Dependencies
```python
numpy==1.24.3          # Numerical computing
pandas==2.0.3          # Data manipulation
matplotlib==3.7.2      # Visualization
seaborn==0.12.2        # Statistical visualization
scikit-learn==1.3.0    # Machine learning
requests==2.31.0       # HTTP requests for data download
```

### Python Version
- Python 3.8 or higher

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/visurarodrigo/medical-insurance-analysis.git
   cd medical-insurance-analysis
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn jupyter requests
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook insurance_analysis.ipynb
   ```

5. **Run the analysis**
   - Execute cells sequentially (Shift + Enter)
   - Dataset will be downloaded automatically
   - All visualizations will be generated inline

## 📊 Sample Visualizations

The notebook includes professional visualizations:
- Distribution plots with KDE overlays
- Box plots for outlier detection
- Scatter plots with regression lines
- Correlation heatmaps
- Model comparison charts
- Actual vs. Predicted performance plots

## 💼 Business Applications

### Insurance Industry Use Cases
1. **Premium Calculation**: Accurate risk-based pricing models
2. **Underwriting Decisions**: Data-driven risk assessment
3. **Policy Planning**: Identify high-risk customer segments
4. **Cost Management**: Target preventive health programs
5. **Market Analysis**: Regional pricing strategies

### Potential Extensions
- Integration with real-time underwriting systems
- Mobile app for instant premium quotes
- A/B testing for pricing strategies
- Customer segmentation for targeted marketing

## 📚 References & Resources

- [IBM Data Analysis with Python - Coursera](https://www.coursera.org/learn/data-analysis-with-python)
- [Medical Insurance Dataset - Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance) (CC0 1.0 Universal License)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Regression Analysis - StatQuest](https://www.youtube.com/statquest)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Visura Rodrigo**

- GitHub: [@visurarodrigo](https://github.com/visurarodrigo)
- Project Link: [https://github.com/visurarodrigo/medical-insurance-analysis](https://github.com/visurarodrigo/medical-insurance-analysis)

## 🙏 Acknowledgments

- IBM Skills Network for providing the dataset and course content
- Coursera for the Data Analysis with Python specialization
- The open-source community for excellent Python libraries

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and Python | January 2026

</div>


