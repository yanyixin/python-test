#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print('来看看你的成绩及高了多少')
# name = input('请输入你的名字')
# s1 = float(input('请输入去年的成绩'))
# s2 = float(input('请输入今年的成绩'))
# s3 = float((s2-s1)/s1)
# r = (s2-s1)/s1
# print('恭喜你，%s, 成绩提高了%.1f%%' %(name, s3)) # .1 表示四舍五入保留一位小数点 f表示浮点数

# list 和 tuple 练习

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# print(L[0][0])
# print(L[1][1])
# print(L[2][2])  # list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们

# if else 练习
# age = 12
# if age >= 18:
# 	print('adult')
# elif age >= 6:
# 	print('teenager')
# else:
# 	print ('kid')

# birth = input('birth: ')
# if birth > 2000:
# 	print('00后')
# else:
# 	print('00前')

height = input('请输入你的身高：')
weight = input('请输入你的体重：')
BMI = weight / (height * height)
print('您的 BMI 指数为：%.2f'%BMI)
if BMI > 32:
	print('严重肥胖')
elif BMI >= 28 and BMI < 32:
	print('肥胖')
elif BMI >= 25 and BMI < 28:
	print('过重')
elif BMI >= 18.5 and BMI < 25:
	print('正常')
else :
	print('过轻')	




