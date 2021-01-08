### 1. 修改 mysql 字符集
- `vim /etc/my.cnf` 添加配置段
```
[client]
default_character_set = utf8mb4

[mysql]
default_character_set = utf8mb4
```
- 在 `[mysqld]` 配置段添加配置项
```
character_set_server = utf8mb4
collation_server = utf8mb4_0900_ai_ci
init_connect = "SET NAMES utf8mb4"
```
- 重启 mysql `systemctl start mysqld`
### 2. 验证 mysql 字符集
- 连接 mysql 执行 sql, 并检查返回结果
```
show variables like "character%";
show variables like "collation%";
```
### 3. 增加远程用户
- 连接 mysql 执行 sql
```
create user testuser identified by "fT866jN^";
grant all privileges on testdb.* to "testuser"@"%";
flush privileges;
```