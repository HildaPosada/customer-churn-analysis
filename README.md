# Customer Churn Analysis 📊

**Predicting customer churn for a telecommunications company using machine learning and delivering actionable business insights.**

![Project Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![ML Models](https://img.shields.io/badge/Models-3-orange)
![Accuracy](https://img.shields.io/badge/Best%20Accuracy-80%25-green)

## 🎯 Project Overview

This end-to-end machine learning project builds a **customer churn prediction model** for a telecommunications company. The project combines predictive modeling with comprehensive business analysis to identify high-risk customers and provide data-driven retention strategies.

**Key Deliverables:**
- Predictive ML models with 80%+ accuracy
- Business insights dashboard in Tableau
- SQL-driven exploratory data analysis
- Actionable retention strategies with financial impact analysis

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Development** | GitHub Codespaces, MacBook Pro M2 |
| **Database** | SQLite Online |
| **Analysis & Modeling** | Python (pandas, scikit-learn, XGBoost) |
| **Visualization** | Tableau Public |
| **Data Source** | Kaggle Telco Customer Churn Dataset |

## 📊 Dataset

**Telco Customer Churn Dataset (Kaggle)**
- **Size**: 7,043 customers, 21 features
- **Target**: Binary churn classification (Yes/No)
- **Features**: Demographics, services, contract details, billing information
- **Churn Rate**: 26.6% (1,869 churned customers)

## 🔍 Key Findings

### Exploratory Data Analysis Insights

**Highest Risk Segments:**
- **Month-to-month contracts**: 43% churn rate
- **Fiber optic internet users**: 41% churn rate  
- **Electronic check payment**: Highest churn among payment methods
- **Senior citizens**: Higher churn than younger customers
- **Short tenure customers** (<12 months): Significantly elevated risk

**Financial Impact:**
- **Lost Revenue**: $1.46M annually from churned customers
- **Average Monthly Revenue**: ~$65 per customer
- **Cost of Churn**: High-value customers leaving disproportionately

## 🤖 Model Performance

### Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| **Logistic Regression** | 0.80 | 0.67 | 0.54 | 0.60 | **0.83** |
| **Random Forest** | 0.79 | 0.64 | 0.51 | 0.57 | 0.82 |
| **XGBoost** | 0.77 | 0.58 | 0.52 | 0.55 | 0.82 |

### Feature Importance (Top 5)
1. **Contract Type** (Month-to-month vs Annual)
2. **Tenure** (Customer lifetime with company)
3. **Internet Service** (Fiber optic highest risk)
4. **Payment Method** (Electronic check vs Auto-pay)
5. **Monthly Charges** (Higher charges = higher churn risk)

### Model Selection & Tuning
- **Cross-validation**: 5-fold stratified CV for robust evaluation
- **Hyperparameter tuning**: GridSearchCV (Random Forest) + RandomizedSearchCV (XGBoost)
- **Final model**: Tuned models saved in `models/final_churn_model.pkl`

## 💼 Business Insights & Recommendations

### 🎯 Retention Strategies

**1. Contract Incentives**
- Offer 10-15% discounts for switching to annual contracts
- **Target**: Month-to-month customers (43% churn rate)
- **Expected Impact**: 20-30% reduction in high-risk segment

**2. Service Quality Improvements**
- Address fiber optic service issues causing 41% churn
- Proactive technical support for fiber customers
- Service reliability monitoring and rapid issue resolution

**3. Payment Method Migration**
- Incentivize auto-pay adoption (credit card/bank transfer)
- **Target**: Electronic check users (highest churn group)
- Offer small monthly discounts for auto-pay enrollment

**4. Early Customer Success Program**
- Deploy retention outreach during first 12 months
- **Target**: New customers with <6 months tenure
- Onboarding support and engagement programs

### 💰 Financial Impact

**Current State:**
- Annual churn cost: **$1.46M**
- Average customer value: **$780** (12-month LTV)

**Projected Savings (10% churn reduction):**
- Retained customers: **187 additional**
- Annual revenue saved: **$146K**
- 3-year impact: **$438K**

## 📁 Repository Structure

```
customer-churn-analysis/
├── data/
│   └── telco_customer_churn.csv
├── models/
│   └── final_churn_model.pkl
├── notebooks/
│   ├── notebooks_02_preprocessing.ipynb
│   ├── notebooks_03_logistic_regression.ipynb
│   ├── notebooks_04_model_comparison.ipynb
│   └── notebooks_05_model_selection.ipynb
├── sql/
│   ├── 00_setup.sql
│   ├── 01_churn_overview.sql
│   ├── 02_service_revenue_analysis.sql
│   └── 03_demographics_analysis.sql
└── README.md
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
```

### Quick Start
```python
# Load and explore the data
import pandas as pd
df = pd.read_csv('data/telco_customer_churn.csv')

# Run preprocessing
from src.data_preprocessing import preprocess_data
X_train, X_test, y_train, y_test = preprocess_data(df)

# Load trained model
import pickle
with open('models/final_churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Make predictions
predictions = model.predict(X_test)
```

## 📈 Dashboard & Visualizations

**Tableau Public Dashboard**: [View Live Dashboard](https://public.tableau.com/app/profile/hilda.posada/viz/CustomerChurnAnalysis_17590022655190/CustomerChurnAnalysisDashboard?publish=yes)

**Key Dashboard Components:**
- **Churn Overview**: 26.6% overall churn rate (1,869 of 7,043 customers)
- **Contract Analysis**: Month-to-month customers show 43% churn rate vs 3% for two-year contracts
- **Internet Service Risk**: Fiber optic users at 41% churn risk, DSL at 19%, No internet at 7%
- **Payment Method Risk**: Electronic check users show highest churn rates
- **Customer Segmentation**: New customers (0-12 months) at 47% churn risk
- **Service Impact Analysis**: Customers without add-on services show 30%+ higher churn
- **Financial Impact KPIs**: $1.4M+ annual revenue at risk from 1,869 churned customers
- **Retention ROI**: 10% churn reduction targeting 187 at-risk customers saves $146K annually

## 🎯 Skills Demonstrated

**Technical Skills:**
- End-to-end ML pipeline development
- Feature engineering and selection
- Model comparison and hyperparameter tuning
- Cross-validation and robust evaluation
- SQL-based business analysis

**Business Skills:**
- Stakeholder-focused insight generation
- Financial impact quantification
- Strategic recommendation development
- Executive dashboard design
- Data storytelling and presentation

## 📫 Contact & Portfolio

**GitHub**: [Your GitHub Profile]
**LinkedIn**: [Your LinkedIn Profile]
**Email**: [Your Email]

**Portfolio Highlight**: *"Built a customer churn prediction model achieving 83% ROC-AUC that identified key risk factors, leading to retention strategies projected to save $146K annually through targeted interventions for high-risk customer segments."*

---

**Project Timeline**: **Total Hours**: ~15 hours | **Completion**: September 2025