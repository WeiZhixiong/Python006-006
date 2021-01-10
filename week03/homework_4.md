### 1. INNER JOIN
```
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
```
### 2. LEFT JOIN
```
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
|    2 | table1        | NULL | NULL          |
```
### 3. RIGHT JOIN
```
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
| NULL | NULL          |    3 | table2        |
```
