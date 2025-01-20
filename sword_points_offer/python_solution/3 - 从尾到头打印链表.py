#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 10:16
# @Author: Administrator
# @File: 3 - 从尾到头打印链表.py
# @Project: mianshi
"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。返回从尾部到头部的列表值序列，例如[1,2,3].

"""
from typing import List
class ListNode: # 链表
    def __init__(self,x):
        self.val=x
        self.next=None


"""
解题思路：
假设链表为：1 -> 2 -> 3 -> None。
递归调用栈：
reverse(1) 调用 reverse(2)。
reverse(2) 调用 reverse(3)。
reverse(3) 调用 reverse(None)。
回溯过程：
reverse(None) 返回 []。
reverse(3) 返回 [] + [3] = [3]。
reverse(2) 返回 [3] + [2] = [3, 2]。
reverse(1) 返回 [3, 2] + [1] = [3, 2, 1]。
最终结果：
[3, 2, 1]，即链表从尾到头的值。
"""
# 解题思路视频,具体过程参照上面的方法
# https://www.bilibili.com/video/BV1CK411c7gx?spm_id_from=333.788.videopod.episodes&vd_source=5efd054eda9a99f2a2db007c7b065e54&p=4
class Solution:
    #
    def reversePrint(self,head:ListNode)->List[int]:
        if not head:
            return []
        return self.reversePrint(head.next)+[head.val]




class Solution2:
    # 链表1 -->2 -->3 -->None
    # todo 这里其实是借鉴了栈的概念，先将链表的元素依次存入栈，然后取出即可
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]  # 反转列表
if __name__ == '__main__':

    solution = Solution()
    _list = [3,2,1,0]
    my_list = ListNode(_list)
    print(solution.reversePrint(my_list))