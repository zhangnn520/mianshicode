#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 16:55
# @Author: Administrator
# @File: 13 - 调整数组顺序使奇数位于偶数前面.py
# @Project: mianshi
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变

"""
class Solution:
    def reOrderArray(self,li):
        order_index=0
        for index,i in enumerate(li):
            if i %2==1:# 将奇数从list中删除，然后从头插入数据，偶数保持不变
                del li[index]
                li.insert(order_index,i)
                order_index+=1
        return li

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9]
    solution=Solution()
    print(solution.reOrderArray(my_list))

