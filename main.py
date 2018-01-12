#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('来看看你的成绩及高了多少')
name = input('请输入你的名字')
s1 = float(input('请输入去年的成绩'))
s2 = float(input('请输入今年的成绩'))
s3 = float((s2-s1)/s1)
# r = (s2-s1)/s1
print('恭喜你，%s, 成绩提高了%.1f%%' %(name, s3))
