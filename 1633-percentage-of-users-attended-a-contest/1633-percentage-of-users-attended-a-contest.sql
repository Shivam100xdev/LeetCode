SELECT contest_id,
       ROUND(cnt * 100.0 / total_users, 2) AS percentage
FROM (
    SELECT contest_id, COUNT(DISTINCT user_id) AS cnt
    FROM Register
    GROUP BY contest_id
) AS r,
(
    SELECT COUNT(*) AS total_users
    FROM Users
) AS u
ORDER BY percentage DESC, contest_id ASC;
