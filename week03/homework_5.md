###1. 创建索引
```
ALTER TABLE table1 ADD INDEX id_index(id);
ALTER TABLE Table1 ADD INDEX name_index(name);
ALTER TABLE Table2 ADD INDEX id_index(id);
ALTER TABLE Table2 ADD INDEX name_index(name);
```
###2. 查看索引
```
SHOW INDEX FROM Table1;
SHOW INDEX FROM Table2;
```
###3. 索引是否加快查询速度, 什么情况下加快查询速度
