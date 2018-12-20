#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   005.py
@Time    :   2018/12/20 19:13:31
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''
# 输入三个整数x，y，z，请把这三个数由小到大输出。


def print_numbers(num_li):
    for i in sorted(num_li):
        print(i)


def main():
    num_li = []
    for i in range(0, 3):
        num = eval(input('请输入第%s个数字：' % str(i + 1)))
        num_li.append(num)
    print_numbers(num_li)


if __name__ == '__main__':
    main()
