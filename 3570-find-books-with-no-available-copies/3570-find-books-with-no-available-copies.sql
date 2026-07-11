# Write your MySQL query statement below
SELECT
    lb.book_id
    , lb.title
    , lb.author
    , lb.genre
    , lb.publication_year
    , COUNT(IF(br.record_id IS NOT NULL AND br.return_date IS NULL, 1, NULL)) as current_borrowers 
FROM
    library_books lb
LEFT JOIN borrowing_records br ON lb.book_id = br.book_id
GROUP BY book_id, lb.total_copies
HAVING current_borrowers > 0 AND lb.total_copies = current_borrowers
ORDER BY current_borrowers DESC, lb.title;



-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna