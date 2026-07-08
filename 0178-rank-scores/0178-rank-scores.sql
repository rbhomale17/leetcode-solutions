# Write your MySQL query statement below
SELECT 
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) as "rank"
FROM scores;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna