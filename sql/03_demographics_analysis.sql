-- Churn by gender
SELECT gender, 
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS churn_rate
FROM "Customers"
GROUP BY gender;

-- Churn by Senior Citizen status
SELECT SeniorCitizen, 
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS churn_rate
FROM "Customers"
GROUP BY SeniorCitizen;

-- Churn by Payment Method
SELECT PaymentMethod, 
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS churn_rate
FROM "Customers"
GROUP BY PaymentMethod;

-- Churn by Multiple Lines (phone service add-on)
SELECT MultipleLines,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS churn_rate
FROM "Customers"
GROUP BY MultipleLines;
