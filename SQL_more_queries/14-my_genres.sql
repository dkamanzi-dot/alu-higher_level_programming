-- 14. My genres
-- List all genres for the show "Dexter"
SELECT
    tg.name
FROM
    tv_genres tg
JOIN
    tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN
    tv_shows ts ON tsg.show_id = ts.id
WHERE
    ts.title = 'Dexter'
ORDER BY
    tg.name ASC;
