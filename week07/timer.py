#!/usr/bin/env python3
# coding: utf-8

import time
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timer(func):
    """统计程序执行时间"""
    @wraps(func)
    def decorate(*args, **kwargs):
        logger.info(f"start execute function {func.__name__}.")
        start_time = time.time()
        func_return = func(*args, **kwargs)
        spend_time = time.time() - start_time
        logger.info(f"execute function {func.__name__} end; spend time: {spend_time}s")
        return func_return
    return decorate


@timer
def test(*args, **kwargs):
    logger.info(f"args: {args}; kwargs: {kwargs}")
    time.sleep(1)
    return "200 ok"


if __name__ == "__main__":
    result = test(1, 2, 3, aa=1, bb=2)
    logger.info(f"test result: {result}")
