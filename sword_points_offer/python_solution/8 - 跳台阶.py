#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 15:25
# @Author: Administrator
# @File: 8 - 跳台阶.py
# @Project: mianshi
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
问题分析
基本情况：
如果台阶数为 0，表示没有台阶，只有一种跳法（不跳）。
如果台阶数为 1，只有一种跳法（跳一步）。
如果台阶数为 2，有两种跳法（跳一步 + 跳一步，或者直接跳两步）。
递推关系：
对于 n >= 3 的情况，青蛙的最后一步有两种可能：
跳 1 级台阶，那么前面的跳法是 f(n-1)。
跳 2 级台阶，那么前面的跳法是 f(n-2)。
因此，递推公式为：f(n) = f(n-1) + f(n-2)。
斐波那契数列：
这个问题实际上就是斐波那契数列的变种，初始条件为 f(0) = 1，f(1) = 1，f(2) = 2。
"""
# todo 动态规划方法
from typing import List
class Solution:
    def jump_ways(self,n:int)->int:
        if n==0:
            return 1
        elif n==1:
            return 1
        # 初始化dp数组
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    def jump_ways2(self,n:int)->int:
        if n==0:
            return 1
        elif n==1:
            return 1
        prev1, prev2 = 0, 1
        for i in range(2,n+1):
            current_value = prev1+prev2
            prev1,prev2=prev2,current_value
        return prev2

