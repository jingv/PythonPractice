#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   002.py
@Time    :   2018/12/20 12:05:21
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''


def calculate_bonus(profits):
    bonus = 0
    if profits >= 1000000:
        bonus += (profits - 1000000) * 0.01
        profits = 1000000
    if 600000 <= profits <= 1000000:
        bonus += (profits - 600000) * 0.015
        profits = 600000
    if 400000 <= profits <= 600000:
        bonus += (profits - 400000) * 0.03
        profits = 400000
    if 200000 <= profits <= 400000:
        bonus += (profits - 200000) * 0.05
        profits = 200000
    if 100000 <= profits <= 200000:
        bonus += (profits - 100000) * 0.075
        profits = 100000
    if 0 <= profits <= 100000:
        bonus += profits * 0.1
    else:
        bonus = 0
    return bonus


def main():
    profits = eval(input('输入利润数：'))
    print('奖金数：', calculate_bonus(profits))


if __name__ == '__main__':
    main()
