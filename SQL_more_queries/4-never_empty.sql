-- 4-never_empty.sql
-- Creates the id_not_null table with id defaulting to 1

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
