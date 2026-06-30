-- Write your PostgreSQL query statement below
SELECT
    d.name as "Department",
    e.name as "Employee",
    e.salary as "Salary"
FROM (
        SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId order by salary desc) as rank from Employee
) e
LEFT JOIN 
    Department d
ON d.id = e.departmentId
WHERE rank <= 3
ORDER BY "Salary" DESC




-- | id | name  | salary | departmentid | id | name  | Department | Employee | Salary |
-- | -- | ----- | ------ | ------------ | -- | ----- | ---------- | -------- | ------ |
-- | 4  | Max   | 90000  | 1            | 1  | IT    | IT         | Max      | 1      |
-- | 1  | Joe   | 85000  | 1            | 1  | IT    | IT         | Joe      | 2      |
-- | 6  | Randy | 85000  | 1            | 1  | IT    | IT         | Randy    | 2      |
-- | 2  | Henry | 80000  | 2            | 2  | Sales | Sales      | Henry    | 3      |
-- | 7  | Will  | 70000  | 1            | 1  | IT    | IT         | Will     | 4      |
-- | 5  | Janet | 69000  | 1            | 1  | IT    | IT         | Janet    | 5      |
-- | 3  | Sam   | 60000  | 2            | 2  | Sales | Sales      | Sam      | 6      |

/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/