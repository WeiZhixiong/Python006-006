#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mysql_host = "192.168.136.128"
mysql_port = 3306
mysql_user = "testuser"
mysql_password = "fT866jN^"
mysql_db = "testdb"
db_url = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}?charset=utf8mb4"
user_table = "user"
asset_table = "asset"
audit_table = "audit"

Base = declarative_base()


class UserTable(Base):
    __tablename__ = user_table
    user_id = Column(Integer(), primary_key=True, nullable=False)
    user_name = Column(String(50), nullable=False, unique=True)
    create_time = Column(DateTime(), default=datetime.now)


class AssetTable(Base):
    __tablename__ = asset_table
    user_id = Column(Integer(), primary_key=True, nullable=False)
    total_asset = Column(Integer, nullable=False)
    update_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class AuditTable(Base):
    __tablename__ = audit_table
    trade_id = Column(Integer(), autoincrement=True, primary_key=True, nullable=False)
    trade_time = Column(DateTime(), nullable=False)
    from_user_id = Column(Integer(), nullable=False)
    to_user_id = Column(Integer(), nullable=False)
    trade_asset = Column(Integer, nullable=False)


def init_trade_info(orm_session_maker):

    user_1 = UserTable(
        user_id=1,
        user_name="张三"
    )
    user_2 = UserTable(
        user_id=2,
        user_name="李四"
    )

    user_1_asset = AssetTable(
        user_id=1,
        total_asset=50
    )

    user_2_asset = AssetTable(
        user_id=2,
        total_asset=20
    )

    sqlalchemy_session = orm_session_maker()
    try:
        sqlalchemy_session.add(user_1)
        sqlalchemy_session.add(user_2)
        sqlalchemy_session.add(user_1_asset)
        sqlalchemy_session.add(user_2_asset)
        sqlalchemy_session.flush()
        sqlalchemy_session.commit()
    except Exception as e:
        logger.error(e)
    finally:
        sqlalchemy_session.close()


def transfer_account(orm_session_maker):
    sqlalchemy_session = orm_session_maker(autocommit=False)
    from_user_name = "张三"
    to_user_name = "李四"
    trade_value = 100
    try:

        from_user_id = sqlalchemy_session.query(UserTable.user_id).filter(
            UserTable.user_name == from_user_name,
        ).one()[0]

        to_user_id = sqlalchemy_session.query(UserTable.user_id).filter(
            UserTable.user_name == to_user_name,
        ).one()[0]

        from_user_asset_entity = sqlalchemy_session.query(AssetTable).filter(
            AssetTable.user_id == from_user_id,
        ).one()

        to_user_asset_entity = sqlalchemy_session.query(AssetTable).filter(
            AssetTable.user_id == to_user_id,
        ).one()

        if from_user_asset_entity.total_asset >= trade_value:
            from_user_asset_entity.total_asset -= trade_value
            to_user_asset_entity.total_asset += trade_value
            audit_record = AuditTable(
                trade_time=datetime.now(),
                from_user_id=from_user_id,
                to_user_id=to_user_id,
                trade_asset=trade_value
            )
            sqlalchemy_session.add(audit_record)
        else:
            logger.error(f"{from_user_name} 账户余额不足, 转账失败")

        sqlalchemy_session.flush()
        sqlalchemy_session.commit()

    except Exception as e:
        logger.error(e)
        sqlalchemy_session.rollback()
    finally:
        sqlalchemy_session.close()


def main():
    sqlalchemy_engine = create_engine(db_url, echo=True, encoding="utf-8")
    # 创建表
    Base.metadata.create_all(sqlalchemy_engine)
    orm_session_maker = sessionmaker(bind=sqlalchemy_engine)
    # 插入基础数据
    init_trade_info(orm_session_maker)
    # 交易
    transfer_account(orm_session_maker)


if __name__ == "__main__":
    main()
