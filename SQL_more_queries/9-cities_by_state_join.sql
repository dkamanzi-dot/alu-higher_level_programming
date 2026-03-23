-- List all cities and their corresponding state names in the database hbtn_0d_usa
-- Display columns: cities.id, cities.name, states.name
-- Results sorted by cities.id in ascending order

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
