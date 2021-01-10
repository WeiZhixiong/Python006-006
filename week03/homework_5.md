### 1. 创建索引
```
ALTER TABLE table1 ADD INDEX id_index(id);
ALTER TABLE Table1 ADD INDEX name_index(name);
ALTER TABLE Table2 ADD INDEX id_index(id);
ALTER TABLE Table2 ADD INDEX name_index(name);
```
### 2. 查看索引
```
SHOW INDEX FROM Table1;
SHOW INDEX FROM Table2;
```
### 3. 索引是否加快查询速度, 什么情况下加快查询速度
- 在只有极少量数据的情况下观察不到查询速度的提升
- 索引就像图书的目录一样，在大量数据的情况下可以有效提高查询速度
- 索引可能会大大提高 select 效率，但也会降低 insert 和 update 的效率，所以不是越多越好
- 在大量非重复的列，使用 =、>、<、>=、<=、between 返回一个范围值的查询情况下，索引可以大大提高查询效率
