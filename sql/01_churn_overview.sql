-- Churn distribution
SELECT Churn, COUNT(*) AS count
FROM "Customers"
GROUP BY Churn;

-- Churn rate by Contract type
SELECT Contract,
       ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 2) AS churn_rate
FROM "Customers"
GROUP BY Contract;

-- Average monthly charges by churn
SELECT Churn, ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge
FROM "Customers"
GROUP BY Churn;

-- Tenure vs churn
SELECT Churn, ROUND(AVG(tenure), 1) AS avg_tenure
FROM "Customers"
GROUP BY Churn;

