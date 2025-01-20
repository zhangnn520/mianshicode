#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 16:34
# @Author: Administrator
# @File: 12 - 数值的整数次方.py
# @Project: mianshi
"""
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
保证base和exponent不同时为0
"""
class Solution:
    def Power(self,base,exponent):
        # 考虑base 为0的情况
        if base==0:
            return 0
        # 考虑指数为0的情况
        if exponent==0:
            return 1

        isNagetive = False
        if exponent<0:# 指数为负，这里需要将其变成正，方便后续计算
            isNagetive = True
            exponent=-exponent
        # 递归求解快速幂，复杂度O(log₂N),其实这里方便计算base*base其实就是base 平方，
        # 整好结合exponent // 2变成整好变成exponent次方。
        p = self.Power(base * base, exponent // 2)
        if exponent % 2 == 1:
            # 如果 exponent 是奇数，p 是 (base^2)^(exponent // 2)，还需要乘上一个 base，从而得出正确的结果。
            # 例如：对于 base^5，可以分解为 base * (base^2)^2，这时需要多乘一个 base。
            p = base * p

        return 1 / p if isNagetive else p