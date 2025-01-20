#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 9:08
# @Author: Administrator
# @File: 1 - 二维数组中的查找.py
# @Project: mianshi
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
# todo 解题思路在与判断对角线数据是否与目标数据大小，大于说明在对角线左侧，此时需要进列数减一，小于说明目标数值在对角线右侧，此时需要行加1

from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        r = 0 # todo r 代表行数
        c = len(matrix[0]) - 1 # todo 代表列数

        while r < len(matrix) and c >= 0:
            if matrix[r][c] < target:# 大于的情况
                # 第一行斜对角线第一值，如果对角线值大于目标值在对角线左侧，小于在右侧，如果等于那就是它自身
                r += 1
            elif matrix[r][c] > target:# 小于的情况
                c -= 1
            else:# 正好等于的情况
                return True
        return False


def generate_sorted_2d_array(m, n):
    # 初始化一个 m x n 的二维数组
    array = [[0 for _ in range(n)] for _ in range(m)]

    # 初始值
    current_value = 1

    # 填充数组
    for i in range(m):
        for j in range(n):
            array[i][j] = current_value
            current_value += 1

    return array




if __name__ == '__main__':
    # 示例：生成一个 3x4 的二维数组
    # m, n = 4, 5
    # result = generate_sorted_2d_array(m, n)
    #
    # 打印结果
    # for row in result:
    #     print(row)
    my_list = [
        [1,   2,  3,  4,  5],
        [6,   7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    solution=Solution()
    solution.findNumberIn2DArray(my_list,target=52)