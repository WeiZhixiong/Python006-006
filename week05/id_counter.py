#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis

redis_host = "192.168.136.128"
redis_port = 6379
redis_db = 0
redis_password = "Abc123456."

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


def counter(video_id):
    redis_conn = get_redis_conn()
    with redis_conn:
        count_number = redis_conn.incr(video_id, 1)
    return count_number


def test():
    print(counter(1001))
    print(counter(1001))
    print(counter(1002))
    print(counter(1001))
    print(counter(1002))


if __name__ == "__main__":
    test()
