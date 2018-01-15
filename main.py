#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print('来看看你的成绩及高了多少')
# name = input('请输入你的名字')
# s1 = float(input('请输入去年的成绩'))
# s2 = float(input('请输入今年的成绩'))
# s3 = float((s2-s1)/s1)
# r = (s2-s1)/s1
# print('恭喜你，%s, 成绩提高了%.1f%%' %(name, s3)) # 1f 表示小数点后一位的浮点数

# list 和 tuple 练习

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])  # list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们