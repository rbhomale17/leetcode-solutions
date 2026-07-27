# Write your MySQL query statement below
SELECT E2.name as 'Employee'
FROM Employee E2
JOIN Employee E1 ON E1.id = E2.managerId
WHERE E2.salary > E1.salary

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna