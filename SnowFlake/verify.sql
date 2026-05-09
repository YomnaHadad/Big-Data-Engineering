USE WAREHOUSE Diamonds_WH;
USE DATABASE Diamonds_DB;
USE SCHEMA STAR_SCHEMA;

SELECT 'dim_cut' AS table_name, COUNT(*) AS row_count FROM dim_cut
UNION ALL
SELECT 'dim_color', COUNT(*) FROM dim_color
UNION ALL
SELECT 'dim_clarity', COUNT(*) FROM dim_clarity
UNION ALL
SELECT 'dim_date', COUNT(*) FROM dim_date
UNION ALL
SELECT 'fact_diamond', COUNT(*) FROM fact_diamonds;

SELECT COUNT(*) FROM fact_diamonds;
SELECT * FROM fact_diamonds LIMIT 15;
SELECT * FROM dim_cut;
SELECT * FROM dim_color;
SELECT * FROM dim_clarity;
SELECT * FROM dim_date;
