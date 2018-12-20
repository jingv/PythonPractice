#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   004.py
@Time    :   2018/12/20 12:44:00
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''
# 输入某年某月某日，判断这一天是这一年的第几天？


def the_num_day(string):
    # 如果字符长度不符合规范， 返回错误信息
    if len(string) != 8:
        return "输入有误"
    num = 0
    try:
        year = int(string[:4])
        month = int(string[4: 6])
        day = int(string[6:])
    except Exception:
        return '输入有误'
    # print(year, ' ', month, ' ', day)
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    # 判断输入的日期是否合法
    if (not (1 <= month <= 12)) or (month == 2 and day > 28) or \
            (month in month_31 and day > 31) or \
            (month in month_30 and day > 30):
        return '输入有误'

    for i in range(1, month):
        if i in month_31:
            num += 31
        if i in month_30:
            num += 30
        if i == 2:
            num += 28
    if year % 4 == 0:
        num += 1
    num += day
    return num


def main():
    date = input('请输入日期：')
    print(the_num_day(date))


if __name__ == '__main__':
    main()
