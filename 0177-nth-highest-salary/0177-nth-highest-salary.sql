CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT salary FROM
        (
            SELECT salary, 
            DENSE_RANK() OVER (ORDER BY salary desc) as RNK 
            -- DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
            FROM Employee 
        ) as rr
        WHERE RNK = N
        LIMIT 1
  );
END

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna