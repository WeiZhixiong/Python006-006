#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps
import logging
import redis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis_host = "redis-host"
redis_port = 6379
redis_db = 0
redis_password = "*************"

redis_pool = redis.ConnectionPool(
    host=redis_host,
    port=redis_port,
    db=redis_db,
    password=redis_password,
    max_connections=10,
)


def get_redis_conn():
    redis_conn = redis.Redis(connection_pool=redis_pool)
    return redis_conn


def send_times(times):

    def decorate(func):
        wraps(func)

        def wrapper(telephone_number, content):
            redis_conn = get_redis_conn()
            with redis_conn:
                send_count = redis_conn.get(telephone_number)
                if not send_count:
                    redis_conn.set(telephone_number, 0, ex=60)
                    send_count = 0
                else:
                    send_count = int(send_count.decode("utf-8"))

                if send_count < times:
                    func(telephone_number, content)
                    redis_conn.incr(telephone_number)
                else:
                    print(f"1 分钟内发送次数超过 {times} 次, 请等待 1 分钟")
                    logger.info(f"1 分钟内发送次数超过 {times} 次, 请等待 1 分钟, "
                                f"telephone: {telephone_number}, "
                                f"发送次数: {send_count}")

        return wrapper

    return decorate


@send_times(times=5)
def sendsms(telephone_number, content):
    content_len = len(content)
    # 单条短信长度限制
    per_len_limit = 70

    # 根据短信内容长度, 直接发送或者分条发送
    if content_len > per_len_limit:
        start_point = 0
        step_len = per_len_limit
        end_point = step_len
        while content_len > start_point:
            content_part = content[start_point:end_point]
            print(f"发送信息: {content_part}")
            start_point = end_point
            end_point = start_point + step_len
    else:
        print(f"发送信息: {content}")

    print("发送成功")
    logger.info(f"发送成功, telephone: {telephone_number}")


def test():
    sendsms(12345654321, content="hello")
    sendsms(12345654321, content="hello")
    sendsms(12345654321, content="hello")
    sendsms(12345654321, content="hello")
    sendsms(12345654321, content="hello")
    sendsms(88887777666, content="hello")
    sendsms(12345654321, content="hello")
    sendsms(88887777666, content="hello")


if __name__ == "__main__":
    test()
