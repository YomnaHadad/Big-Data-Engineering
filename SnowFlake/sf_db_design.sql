CREATE OR REPLACE WAREHOUSE Diamonds_WH
WITH WAREHOUSE_SIZE = "XSMALL"
AUTO_SUSPEND = 60
AUTO_RESUME = TRUE
INITIALLY_SUSPENDED = TRUE;

CREATE OR REPLACE DATABASE Diamonds_DB;
CREATE OR REPLACE SCHEMA Diamonds_DB.STAR_SCHEMA;

-- TABLES --
CREATE TABLE dim_cut (
    cut_id INT,
    cut_name STRING
);

CREATE TABLE dim_color (
    color_id INT,
    color_name STRING
);

CREATE TABLE dim_clarity (
    clarity_id INT,
    clarity_name STRING
);

CREATE TABLE dim_date (
    date_id INT,
    quarter INT,
    day INT,
    month INT,
    year INT,
    full_date TIMESTAMP
);

CREATE TABLE fact_diamonds (
    -- diamond_fact_id INT AUTOINCREMENT PRIMARY KEY,

    cut_id INT,
    color_id INT,
    clarity_id INT,
    date_id INT,

    carat DOUBLE,
    depth DOUBLE,
    table_percentage DOUBLE,

    length_mm DOUBLE,
    width_mm DOUBLE,
    depth_mm DOUBLE,

    volume_mm3 DOUBLE,

    depth_pct_calc DOUBLE,
    depth_diff DOUBLE,

    price INT,
    price_per_carat DOUBLE,

    processed_timestamp TIMESTAMP
);

USE WAREHOUSE Diamonds_WH;
USE DATABASE Diamonds_DB;
USE SCHEMA STAR_SCHEMA;
