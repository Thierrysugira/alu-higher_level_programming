# SQL - Introduction

This directory contains SQL scripts to create and manage databases and
tables in MySQL, and to insert, update, delete and query rows.

Run a script with, for example:

    cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
    cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

| File | Description |
| ---- | ----------- |
| `0-list_databases.sql` | Lists all databases of the MySQL server. |
| `1-create_database_if_missing.sql` | Creates `hbtn_0c_0` if it does not exist. |
| `2-remove_database.sql` | Deletes `hbtn_0c_0` if it exists. |
| `3-list_tables.sql` | Lists the tables of a database. |
| `4-first_table.sql` | Creates `first_table` if it does not exist. |
| `5-full_table.sql` | Prints the full description of `first_table`. |
| `6-list_values.sql` | Lists all rows of `first_table`. |
| `7-insert_value.sql` | Inserts a row in `first_table`. |
| `8-count_89.sql` | Counts the rows with `id = 89`. |
| `9-full_creation.sql` | Creates `second_table` and adds four rows. |
| `10-top_score.sql` | Lists `second_table` by best score. |
| `11-best_score.sql` | Lists the records with a score of 10 or more. |
| `12-no_cheating.sql` | Updates the score of Bob by name. |
| `13-change_class.sql` | Removes the records with a score of 5 or less. |
| `14-average.sql` | Computes the average score. |
| `15-groups.sql` | Counts the records per score. |
| `16-no_link.sql` | Lists the records that have a name. |
| `100-move_to_utf8.sql` | Converts the database, `first_table` and its fields to UTF8. |
| `101-avg_temperatures.sql` | Average temperature by city, highest first. |
| `102-top_city.sql` | Top 3 cities by temperature in July and August. |
| `103-max_state.sql` | Maximum temperature of each state. |
