-- Churn by Internet Service
SELECT InternetService,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS churn_rate
FROM "Customers"
GROUP BY InternetService;

-- Churn by Payment Method
SELECT PaymentMethod,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS churn_rate
FROM "Customers"
GROUP BY PaymentMethod;

-- Revenue lost from churners
SELECT Churn, ROUND(SUM(MonthlyCharges), 2) AS total_revenue
FROM "Customers"
GROUP BY Churn;
