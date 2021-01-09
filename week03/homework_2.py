#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import desc, and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mysql_host = "192.168.136.128"
mysql_port = 3306
mysql_user = "testuser"
mysql_password = "***********"
mysql_db = "testdb"
user_table = "user"
db_url = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}?charset=utf8mb4"

Base = declarative_base()


class UserTable(Base):
    __tablename__ = user_table
    user_id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    age = Column(Integer())
    birthday = Column(Date(), nullable=False)
    sex = Column(String(10))
    education = Column(String(50))
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return (f"{self.user_id}, {self.name}, {self.age}, {self.birthday}, "
                f"{self.sex}, {self.education}, {self.education}, "
                f"{self.create_time}, {self.update_time}")


def sqlalchemy_test():
    sqlalchemy_engine = create_engine(db_url, echo=True, encoding="utf-8")
    # create table
    Base.metadata.create_all(sqlalchemy_engine)

    sqlalchemy_session = sessionmaker(bind=sqlalchemy_engine)()

    # insert user
    user_1 = UserTable(
        user_id=1,
        name="小明",
        age=20,
        birthday="2001-01-01",
        sex="男",
        education="本科"
    )
    user_2 = UserTable(
        user_id=2,
        name="小红",
        age=19,
        birthday="2002-12-21",
        sex="女",
        education="本科"
    )
    user_3 = UserTable(
        user_id=3,
        name="小白",
        age=18,
        birthday="2003-01-03",
        sex="女",
        education="本科"
    )
    sqlalchemy_session.add(user_1)
    sqlalchemy_session.add(user_2)
    sqlalchemy_session.add(user_3)
    sqlalchemy_session.flush()
    sqlalchemy_session.commit()

    #query all
    all_user = sqlalchemy_session.query(UserTable).all()
    for user in all_user:
        print(user)

    # 指定条件查询
    result = sqlalchemy_session.query(UserTable.name).filter(UserTable.user_id == 1).first()
    print(result)

    # 排序
    result = sqlalchemy_session.query(UserTable).order_by(desc(UserTable.age))
    for user in result:
        print(user.name)

    # 连接词
    result = sqlalchemy_session.query(UserTable).filter(
       or_(
           UserTable.age == 20,
           UserTable.age.between(17, 18)
       )
    )
    for user in result:
        print(user)


def pymysql_test():
    pymysql_conn = pymysql.connect(
        user=mysql_user,
        password=mysql_password,
        host=mysql_host,
        database=mysql_db,
        port=mysql_port
    )

    insert_user_sql = "insert into user (user_id, name, age, birthday, sex, " \
                      "education, create_time, update_time) values (%s, %s, %s, %s, %s, %s, %s, %s)"

    try:

        # 插入数据
        with pymysql_conn.cursor() as cursor:
            user_tuple = (
                (4, "晓南", 20, "2001-01-01", "男", "本科", datetime.now(), datetime.now()),
                (5, "小丽", 21, "2000-01-01", "女", "本科", datetime.now(), datetime.now()),
                (6, "小黑", 23, "2000-01-01", "女", "研究生", datetime.now(), datetime.now()),
            )
            result = cursor.executemany(insert_user_sql, user_tuple)
            logger.info(f"insert user count {result}")
        pymysql_conn.commit()

        # 查询
        with pymysql_conn.cursor() as cursor:
            query_sql = "select * from user"
            cursor.execute(query_sql)
            query_result = cursor.fetchall()
            for user in query_result:
                print(user)

    except Exception as e:
        logger.error(e)
    finally:
        pymysql_conn.close()


def main():
    sqlalchemy_test()
    pymysql_test()


if __name__ == "__main__":
    main()
