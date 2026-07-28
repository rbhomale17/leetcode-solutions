# Write your MySQL query statement below
SELECT
    activity_date as day,
    COUNT(DISTINCT(user_id)) as active_users
FROM
    Activity
WHERE activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY) 
    AND activity_date <= '2019-07-27'
GROUP BY activity_date

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna