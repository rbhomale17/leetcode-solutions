# Write your MySQL query statement below
SELECT 
    *
FROM
    Users
WHERE
    REGEXP_LIKE(email, '^[A-Za-z0-9_]+@[A-Za-z]+\\.com$')
ORDER BY user_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna