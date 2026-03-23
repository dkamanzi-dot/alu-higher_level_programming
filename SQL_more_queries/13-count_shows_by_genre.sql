-- 13. Number of shows by genre
-- List all genres with count of linked shows, ordered descending
SELECT
    tg.name AS genre,
    COUNT(tsg.show_id) AS number_of_shows
FROM
    tv_genres tg
JOIN
    tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY
    tg.name
ORDER BY
    number_of_shows DESC;
