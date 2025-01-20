# -*- coding: utf-8 -*-
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39。
"""
from typing import List


class Solution:
    def fibonacci(self,n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # 初始化前两个值
        prev1, prev2 = 0, 1

        # 迭代计算,这里是从数据2开始的，因为前面0和1的情况已经讨论过了。
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return prev2

if __name__ == '__main__':
    solution = Solution()
    result =solution.fibonacci(5)
    print(result)