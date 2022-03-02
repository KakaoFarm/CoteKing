/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT U.name, R.distance_sum
FROM USERS U
JOIN (SELECT user_id, SUM(distance) as distance_sum
    FROM RIDES
    GROUP BY user_id) R
ON U.id = R.user_id
ORDER BY R.distance_sum DESC, U.name ASC
LIMIT 100;
