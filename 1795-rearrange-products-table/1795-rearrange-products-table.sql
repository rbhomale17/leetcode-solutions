# Write your MySQL query statement below
SELECT product_id, 'store1' as store, store1 as price FROM products WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2' as store, store2 as price FROM products WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' as store, store3 as price FROM products WHERE store3 IS NOT NULL
ORDER BY product_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna