-- -- -- Write your PostgreSQL query statement below
-- -- First solution

-- SELECT 
--     total.Day , 
--     -- calculate the rate of cancellation
--     ROUND(1.0 * COALESCE(cancelled.cancelled_trips, 0) / total.total_trips, 2) as "Cancellation Rate"
-- from (
--     -- FIND totol count as per clause first
-- select request_at as Day, COUNT(*) as total_trips  from trips t
-- JOIN Users uc ON uc.users_id = t.client_id
-- JOIN Users ud ON ud.users_id = t.driver_id
-- where (uc.banned = 'No' AND ud.banned = 'No')
-- AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
-- GROUP BY request_at
-- ) total 
-- LEFT JOIN (
--     -- find cancelled cound as per clause and the join using day
-- select request_at as Day, COUNT(*) as cancelled_trips  from trips t
-- JOIN Users uc ON uc.users_id = t.client_id
-- JOIN Users ud ON ud.users_id = t.driver_id
-- where (uc.banned = 'No' AND ud.banned = 'No')
-- AND request_at BETWEEN '2013-10-01' AND '2013-10-03' AND status LIKE 'cancelled%'
-- GROUP BY request_at
-- ) cancelled
-- -- join by date
-- ON total.Day = cancelled.Day
-- order by total.Day;


-- -- Second solution
SELECT 
    request_at as "Day",
    ROUND(1.0 * SUM(CASE WHEN status LIKE 'cancelled%' THEN 1 ELSE 0 END) / COUNT(*), 2) AS "Cancellation Rate"
    -- *
FROM Trips t
JOIN Users uc ON uc.users_id = t.client_id
JOIN Users ud ON ud.users_id = t.driver_id
where uc.banned = 'No' 
AND ud.banned = 'No'
AND request_at BETWEEN '2013-10-01' AND '2013-10-03' 
GROUP BY request_at
-- ORDER BY request_at

/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/