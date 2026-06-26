# Write your MySQL query statement below

-- Normal approach
SELECT id,
CASE
    WHEN p_id IS NULL THEN "Root"
    WHEN id IN (SELECT DISTINCT p_id FROM tree) THEN "Inner"
    ELSE "Leaf"
END AS type
FROM tree

-- -- Join method
-- SELECT DISTINCT id,
-- CASE
--     WHEN p_id IS NULL THEN "Root"
--     WHEN pt IS NULL THEN "Leaf"
--     ELSE "Inner"
-- END AS type
-- FROM (
--     SELECT t.id , t.p_id, pt.id as pt
--     FROM tree t
--     LEFT JOIN tree pt ON pt.p_id = t.id
-- ) as sub



-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna