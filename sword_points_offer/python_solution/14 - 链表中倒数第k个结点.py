#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 17:22
# @Author: Administrator
# @File: 14 - 链表中倒数第k个结点.py
# @Project: mianshi
"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None

        p1, p2 = head, head
        # p1先走k步,若k大于链表长度，返回None
        while k:
            if p1:
                p1 = p1.next
                k -= 1
            else:
                return None

        # p1, p2同时往前走，当p1到达链表尾部时，p2刚好在倒数第k个位置
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2