#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mapper(func, *args):

    # 传入参数的可迭代对象列表
    arg_iter_obj_list = []

    # 将要传给 func 的参数列表
    send_func_arg_list = []

    # 获取可迭代对象并加入可迭代对象列表
    for arg in args:
        arg_iter_obj_list.append(iter(arg))

    while True:
        for arg_iter_obj in arg_iter_obj_list:
            try:
                send_func_arg_list.append(next(arg_iter_obj))
            except StopIteration:
                return None
        yield func(*send_func_arg_list)
        send_func_arg_list = []


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
