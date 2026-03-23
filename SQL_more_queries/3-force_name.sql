-- 3-force_name.sql
-- Creates force_name table with non-nullable name column

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
