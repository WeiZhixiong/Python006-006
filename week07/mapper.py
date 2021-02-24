#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mapper(func, *args):

    for args in zip(*args):
        yield func(*args)


def awesome_add(x, y, z):
    return f"result: {x}, {y}, {z}"


def test():
    l1 = [1, 2, 3, 4]
    l2 = range(5, 19)
    l3 = (4, 5, 6)
    # 异常测试
    # m = mapper(awesome_add, l1, l2)
    m = mapper(awesome_add, l1, l2, l3)
    for i in m:
        print(i)


if __name__ == "__main__":
    test()
