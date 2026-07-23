# Write your MySQL query statement below
SELECT
    *,
    (dna_sequence LIKE 'ATG%') as has_start,
    (
        dna_sequence LIKE '%TAA' 
        or dna_sequence LIKE '%TAG' 
        or dna_sequence LIKE '%TGA'
    ) as has_stop,
    (dna_sequence LIKE '%ATAT%') as has_atat,
    (dna_sequence LIKE '%GGG%') as has_ggg
FROM
    samples
ORDER BY sample_id ASC




-- # Write your MySQL query statement below
-- SELECT
--     *,
--     (
--         CASE
--             WHEN dna_sequence LIKE 'ATG%' THEN 1
--             ELSE 0
--         END
--     ) as has_start,
--     (
--         CASE
--             WHEN dna_sequence LIKE '%TAA' or dna_sequence LIKE '%TAG' or dna_sequence LIKE '%TGA' THEN 1
--             ELSE 0
--         END
--     ) as has_stop,
--     (
--         CASE
--             WHEN dna_sequence LIKE '%ATAT%' THEN 1
--             ELSE 0
--         END
--     ) as has_atat,
--     (
--         CASE
--             WHEN dna_sequence LIKE '%GGG%' THEN 1
--             ELSE 0
--         END
--     ) as has_ggg
-- FROM
--     samples
-- ORDER BY sample_id ASC


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna