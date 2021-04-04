#### SQL
```
1. SELECT * FROM data;

2. SELECT * FROM data LIMIT 10;

3. SELECT id FROM data;  //id 是 data 表的特定一列

4. SELECT COUNT(id) FROM data;

5. SELECT * FROM data WHERE id<1000 AND age>30;

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

8. SELECT * FROM table1 UNION SELECT * FROM table2;

9. DELETE FROM table1 WHERE id=10;

10. ALTER TABLE table1 DROP COLUMN column_name;
```
#### pandas
```
1. data

2. data[:10]

3. data.id

4. data.id.count()

5. data[(data.id<1000) & (data.age>30)]

6. data[['id', 'order_id']].drop_duplicates().groupby(by='id').count()

7. pd.merge(table1, table2, on='id')

8. pd.merge(table1, table2, how='outer').drop_duplicates()

9. table1 = table1[table1.id!=10]

10. table1 = table1.drop(columns=["id"])
```