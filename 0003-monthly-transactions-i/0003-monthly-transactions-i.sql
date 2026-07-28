# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') as `month`,
    country,
    COUNT(state) as trans_count,
    COUNT(
        CASE
            WHEN state IN ('approved') THEN 1
            ELSE NULL
        END
    ) as approved_count,
    SUM(amount) as trans_total_amount,
    SUM(
        CASE
            WHEN state = 'approved' THEN amount
            ELSE 0
        END
    ) as approved_total_amount
FROM
    Transactions T
GROUP BY country, `month`

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna