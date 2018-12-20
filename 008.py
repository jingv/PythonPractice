#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   008.py
@Time    :   2018/12/20 19:27:02
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''
# 输出9*9口诀表。


def print_multiply_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d * %d = %d' % (j, i, i*j), end=' ')
        print()


def main():
    print_multiply_table()


if __name__ == '__main__':
    main()
