# coding: utf-8

from itemadapter import ItemAdapter
import csv
import pymysql

mysql_host = "my-host"
mysql_port = 3306
mysql_user = "test_user"
mysql_password = "********"
mysql_db = "maoyan"
movie_table = "movie"


class MaoYanPipeline:

    def __init__(self):
        columns = ["movie_name", "movie_type", "show_time"]
        file_name = "movie_list.csv"
        self.file = open(file_name, 'a+', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, columns)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()


class MaoYanMysqlPipeline:

    def __init__(self):
        self.connect = pymysql.connect(
            user=mysql_user,
            password=mysql_password,
            host=mysql_host,
            database=mysql_db,
            port=mysql_port
        )
        self.cursor = self.connect.cursor()

        create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS `{movie_table}` (
               `movie_name` VARCHAR(100) NOT NULL,
               `movie_type` VARCHAR(100) NOT NULL,
               `show_time` VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;    
        """
        self.cursor.execute(create_table_sql)

    def process_item(self, item, spider):
        sql = f"insert into {movie_table} " \
              f"(`movie_name`, `movie_type`, `show_time`) value (%s, %s, %s)"
        self.cursor.execute(
            sql,
            (item["movie_name"], item["movie_type"], item["show_time"],)
        )
        return item

    def close_spider(self, spider):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
