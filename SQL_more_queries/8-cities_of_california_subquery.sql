-- Write a script that lists all the cities of California in the database hbtn_0d_usa
-- Do not use JOIN, use a subquery instead
-- Results sorted by cities.id in ascending order

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
