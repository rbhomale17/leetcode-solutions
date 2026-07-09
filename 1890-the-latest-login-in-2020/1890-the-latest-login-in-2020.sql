# Write your MySQL query statement below
SELECT 
    user_id,
    MAX(time_stamp) as last_stamp          
FROM
    Logins
WHERE 
    YEAR(time_stamp) = 2020
GROUP BY user_id
ORDER BY time_stamp DESC

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna