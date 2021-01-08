### 1. �޸� mysql �ַ���
- `vim /etc/my.cnf` ������ö�
```
[client]
default_character_set = utf8mb4

[mysql]
default_character_set = utf8mb4
```
- �� `[mysqld]` ���ö����������
```
character_set_server = utf8mb4
collation_server = utf8mb4_0900_ai_ci
init_connect = "SET NAMES utf8mb4"
```
- ���� mysql `systemctl start mysqld`
### 2. ��֤ mysql �ַ���
- ���� mysql ִ�� sql, ����鷵�ؽ��
```
show variables like "character%";
show variables like "collation%";
```
### 3. ����Զ���û�
- ���� mysql ִ�� sql
```
create user testuser identified by "fT866jN^";
grant all privileges on testdb.* to "testuser"@"%";
flush privileges;
```