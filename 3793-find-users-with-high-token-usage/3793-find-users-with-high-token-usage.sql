# Write your MySQL query statement below
SELECT
    user_id,
    COUNT(prompt) as prompt_count,
    ROUND(AVG(tokens), 2) as avg_tokens
FROM
    prompts
GROUP BY user_id
HAVING COUNT(prompt) >= 3 AND MAX(tokens) > avg_tokens
ORDER BY avg_tokens DESC, user_id;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna