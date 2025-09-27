# customer-churn-analysis
Build a machine learning model to predict customer churn for a telecommunications company, providing actionable business insights and retention strategies.
## Exploratory Data Analysis (EDA):
Using SQL on the Telco Customer Churn dataset, I explored churn behavior across customer segments, service usage, and revenue impact. Key findings:

Overall churn rate: ~26.6% of customers churned (1,869 out of 7,043).

Contract type:

Month-to-month contracts had the highest churn (~43%).

One-year and two-year contracts showed much lower churn rates.

Internet service:

Fiber optic customers churned at the highest rate (~41%).

DSL customers churned at ~19%.

Customers without internet service churned the least (~7%).

Demographics:

Senior Citizens had higher churn than non-seniors.

Gender was not a strong predictor, with churn nearly equal between male and female.

Payment methods:

Customers using electronic checks had the highest churn rate.

Those paying via credit card or bank transfer had lower churn.

Revenue impact:

Churners contributed significantly to lost monthly revenue, with average charges higher among churners compared to retained customers.

Insight: Customers on short-term contracts, with higher monthly charges, using fiber optic internet, and paying via electronic check are most at risk of churn.

##  Model Selection & Tuning

### Cross-Validation
Performed 5-fold stratified cross-validation across Logistic Regression, Random Forest, and XGBoost.

- Logistic Regression CV ROC-AUC: ~0.83  
- Random Forest CV ROC-AUC: ~0.82  
- XGBoost CV ROC-AUC: ~0.82  

### Hyperparameter Tuning
- **Random Forest**: GridSearchCV over `n_estimators`, `max_depth`, and `min_samples_split`.  
- **XGBoost**: RandomizedSearchCV over `n_estimators`, `max_depth`, `learning_rate`, `subsample`, and `colsample_bytree`.  

Best parameters improved model stability and generalization.

### Feature Importance
- **Random Forest**: Tenure, TotalCharges, and MonthlyCharges were most predictive.  
- **XGBoost**: Contract type (1-yr, 2-yr), Fiber optic internet, and payment method strongly impacted churn likelihood.  

### Final Model Evaluation (Test Set)
| Model          | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|----------------|----------|-----------|--------|----------|---------|
| Random Forest  | 0.79     | 0.64      | 0.51   | 0.57     | 0.82    |
| XGBoost        | 0.77     | 0.58      | 0.52   | 0.55     | 0.82    |

### Key Insights
- Customers on **month-to-month or short contracts** are more likely to churn.  
- **Fiber optic internet** users show higher churn risk than DSL or no internet.  
- **Electronic check** payment users churn more than credit card/automatic bank transfer.  
- Shorter **tenure** and higher **monthly charges** also increase churn risk.  

### Deliverable
- Final tuned model saved as: models/final_churn_model.pkl
