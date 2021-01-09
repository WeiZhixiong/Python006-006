###1. INNER JOIN 结果
```
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
```
###2. LEFT JOIN 结果
```
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
|    2 | table1        | NULL | NULL          |
```
###3. RIGHT JOIN 结果
```
| id   | name          | id   | name          |
+------+---------------+------+---------------+
|    1 | table1_table2 |    1 | table1_table2 |
| NULL | NULL          |    3 | table2        |
```
