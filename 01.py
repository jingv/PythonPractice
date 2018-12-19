#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01.py
@Time    :   2018/12/19 20:47:27
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''
# 题目：有1、2、3、4 个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
import copy


def core(num_li, begin=0):
    if begin == len(num_li) - 1:
        print(' '.join(num_li))
    else:
        for i in range(begin, len(num_li)):
            num_li[i], num_li[begin] = num_li[begin], num_li[i]
            core(num_li, begin + 1)
            num_li[i], num_li[begin] = num_li[begin], num_li[i]


def main():
    num_li = [1, 2, 3, 4]
    for i in range(0, len(num_li)):
        num_copy = copy.copy(num_li)
        num_copy.pop(i)
        core([str(i) for i in num_copy])


if __name__ == '__main__':
    main()
