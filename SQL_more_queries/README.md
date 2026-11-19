# SQL - More queries

This directory contains SQL scripts on users and privileges, constraints
(`NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`), subqueries
and joins.

| File | Description |
| ---- | ----------- |
| `0-privileges.sql` | Lists all privileges of the MySQL users user_0d_1 and user_0d_2. |
| `1-create_user.sql` | Creates the user user_0d_1 with all privileges on the MySQL server. |
| `2-create_read_user.sql` | Creates the database hbtn_0d_2 and the user user_0d_2 with read-only access. |
| `3-force_name.sql` | Creates the table force_name where name cannot be null. |
| `4-never_empty.sql` | Creates the table id_not_null where id has the default value 1. |
| `5-unique_id.sql` | Creates the table unique_id where id is unique and defaults to 1. |
| `6-states.sql` | Creates the database hbtn_0d_usa and the table states in it. |
| `7-cities.sql` | Creates the database hbtn_0d_usa and the table cities in it. |
| `8-cities_of_california_subquery.sql` | Lists the cities of California using a subquery. |
| `9-cities_by_state_join.sql` | Lists all cities with the name of their state. |
| `10-genre_id_by_show.sql` | Lists the shows that have at least one genre linked. |
| `11-genre_id_all_shows.sql` | Lists all shows with their genre id, or NULL when there is none. |
| `12-no_genre.sql` | Lists the shows that have no genre linked. |
| `13-count_shows_by_genre.sql` | Lists the genres with the number of shows linked to each. |
| `14-my_genres.sql` | Lists all genres of the show Dexter. |
| `15-comedy_only.sql` | Lists all Comedy shows. |
| `16-shows_by_genre.sql` | Lists all shows and the genres linked to each, or NULL when there is none. |
