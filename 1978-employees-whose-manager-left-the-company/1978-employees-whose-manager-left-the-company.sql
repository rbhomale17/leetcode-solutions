# Write your MySQL query statement below
SELECT E1.employee_id
FROM Employees E1
LEFT JOIN Employees E2 ON E1.manager_id = E2.employee_id
WHERE E1.salary < 30000
    AND E2.employee_id IS NULL
    AND E1.manager_id IS NOT NULL
ORDER BY E1.employee_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna