#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 10:12
# @Author: Administrator
# @File: 2 - 替换空格.py
# @Project: mianshi
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy

"""

class Solution:
    def replace_string(self,string):
        return string.replace(" ","%20")

    def replace_string2(self,string):
        return '%20'.join(string.split(' '))

if __name__ == '__main__':
    my_string = "We Are Happy"
    solution = Solution()
    result =solution.replace_string(my_string)
    print(result)
