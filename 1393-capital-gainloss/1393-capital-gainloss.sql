# Write your MySQL query statement below
SELECT 
    stock_name, 
    SUM(
        CASE WHEN operation = 'Sell' THEN price
        ELSE - price
        END
    ) as capital_gain_loss
FROM stocks
GROUP BY stock_name;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna