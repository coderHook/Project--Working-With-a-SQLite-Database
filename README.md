# Project: Working with SQLite Database

In this project, we'll be working with the CIA World Factbook, a compendium of facts about countries. The Factbook contains demographic information for each country in the world, including:

population - The population as of 2015
population_growth - The annual population growth rate, as a percentage
area - The total land and water area
You can download the Factbook as a SQLite database from GitHub if you want to work with it on your own computer. In this project, we'll be working with Python and the SQLite command line tool (SQLite Command Shell) to connect to the database, extract data, and perform analysis on the data.

## Database Schema / Tables / Columns

CREATE TABLE "facts"(
  "id"   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "code" varchar(255) NOT NULL,
  "name" varchar(255) NOT NULL,

  -----------------------
  -- Geography

  "area"       integer,
  "area_land"  integer,
  "area_water" integer,

  ------------------------
  -- People and Society

  "population"        integer,
  "population_growth" float,
  "birth_rate"        float,
  "death_rate"        float,
  "migration_rate"    float,

  ... )
(Source: factbook.sql)

## Usage

Find the ten largest countries by area:

SELECT name, area FROM facts ORDER BY area DESC LIMIT 10;
Resulting in:

Russia         | 17_098_242
Canada         |  9_984_670
United States  |  9_826_675
China          |  9_596_960
Brazil         |  8_515_770
Australia      |  7_741_220
European Union |  4_324_782
India          |  3_287_263
Argentina      |  2_780_400
Kazakhstan     |  2_724_900

This is a small preview of how this database works.
