#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   003.py
@Time    :   2018/12/20 12:28:33
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''
# 题目：一个整数，它加上100 后是一个完全平方数，再加上168 又是一个完全平方数，请问该数是多少？


def find_num():
    num = 0
    while True:
        num1 = pow((num + 100), 0.5)
        if num1 == int(num1):
            num2 = pow((num + 168), 0.5)
            if num2 == int(num2):
                return num
        num += 1
    return num


def main():
    print(find_num())


if __name__ == '__main__':
    main()
