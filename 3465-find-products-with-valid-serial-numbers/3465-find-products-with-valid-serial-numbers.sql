# Write your MySQL query statement below
SELECT
    *
FROM
    products
WHERE
    REGEXP_LIKE(
        description,  
        '(^|[^A-Za-z0-9])SN[0-9]{4}-[0-9]{4}($|[^A-Za-z0-9])',
        'c'
    )
ORDER BY product_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna