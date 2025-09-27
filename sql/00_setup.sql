-- Check all tables
SELECT name FROM sqlite_master WHERE type='table';

-- Use the exact table name (capital C)
SELECT COUNT(*) FROM "Customers";

-- Preview first rows
SELECT * FROM "Customers" LIMIT 5;
