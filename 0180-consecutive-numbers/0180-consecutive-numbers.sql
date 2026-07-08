# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums 
FROM (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) as num1,
        LAG(num, 2) OVER (ORDER BY id) as num2
    FROM
        Logs
) as nums
WHERE nums.num = nums.num1 and nums.num = nums.num2

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna