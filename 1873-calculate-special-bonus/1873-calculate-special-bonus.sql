# Write your MySQL query statement below
SELECT
    -- *,
    employee_id,
    CASE
        WHEN employee_id % 2 != 0 AND name NOT LIKE 'M%'
        THEN salary
        ELSE 0
    END as bonus
FROM
    Employees
ORDER BY employee_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna