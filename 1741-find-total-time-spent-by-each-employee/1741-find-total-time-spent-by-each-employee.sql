# Write your MySQL query statement below
SELECT
    event_day as 'day',
    emp_id,
    ABS(SUM(in_time) - SUM(out_time)) as total_time
FROM
    Employees
GROUP BY emp_id, event_day

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna