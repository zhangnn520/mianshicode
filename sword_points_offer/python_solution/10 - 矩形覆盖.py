#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 16:07
# @Author: Administrator
# @File: 10 - 矩形覆盖.py
# @Project: mianshi
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
from typing import List
class Solution:
    def rectCover(self,n:int)->int:
        if n<=2:
            return n
        pre1,pre2=1,2
        for i in range(3,n+1):
            current_value =pre1+pre2
            pre1,pre2=pre2,current_value
        return pre2