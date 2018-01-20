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

# height = float(input('请输入你的身高(m)：'))
# weight = float(input('请输入你的体重(kg)：'))
# BMI = weight / (height * height)
# print('您的 BMI 指数为：%.2f'%BMI)
# if BMI < 18.5:
# 	print('过轻')
# elif BMI < 25:
# 	print('正常')
# elif BMI < 28:
# 	print('过重')
# elif BMI < 32:
# 	print('肥胖')
# else :
# 	print('严重肥胖')	
	
# 循环
# sum = 0
# for x in list(range(101)):
# 	sum = sum + x
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
# 	print('hello %s'%name) # %s 表示格式化字符串

# n = 1
# while n < 100:
# 	if n > 10:
# 		break
# 	print(n)
# 	n = n + 1
# print('end')	

# number = 0
# while number < 10:
# 	number = number + 1
# 	if number % 2 == 0:
# 		continue
# 	print(number)

# list=['coy','mandy','jack']
# s=set(list)
# list.append('Vokkor')
# print(s)

# 函数
# print(abs(-20)) # 求绝对值

# a1 = 255
# print(hex(a1)) # hex() 函数表示转化成 16 进制

# 定义函数
# def my_abs(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x

# print(my_abs(-100))

# import math
# def quadratic(a, b, c):
# 	pass

# print('quadratic', quadratic())

# def add_end(l = None):
# 	if l is None:
# 		l = []
# 	l.append('end')
# 	return l
# print(add_end([1,2]))

# 可变参数
# nums = [1,2,3]
# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + n * n
# 	return sum
# print(calc())

# # 关键字参数
# other = {'love': 'music', 'city': 'shanghai'}
# def person(name, age, *, love, city):
# 	print('name:', name, 'age:', age, 'love:', love)
# person('ym', 18, **other)

def product(*nums):
	if len(nums)  == 0:
		raise TypeError
	else:
		sum = 1
		for n in nums:
			sum = sum * n
		return int(sum)
# print(product(2,2,3))

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('5测试失败!')
elif product(5, 6) != 30:
    print('5,6测试失败!')
elif product(5, 6, 7) != 210:
    print('5,6,7测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('5,6,7,9测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')





