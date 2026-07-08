# Write your MySQL query statement below
-- SELECT DISTINCT num as ConsecutiveNums 
-- FROM (
--     SELECT
--         num,
--         LAG(num, 1) OVER (ORDER BY id) as num1,
--         LAG(num, 2) OVER (ORDER BY id) as num2
--     FROM
--         Logs
-- ) as nums
-- WHERE nums.num = nums.num1 and nums.num = nums.num2


SELECT DISTINCT l1.num as ConsecutiveNums
FROM Logs l1, logs l2, logs l3
WHERE
    l1.id = l2.id - 1 AND l1.id = l3.id - 2
    AND l1.num = l2.num AND l1.num = l3.num

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna