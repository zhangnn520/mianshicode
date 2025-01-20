#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 13:40
# @Author: Administrator
# @File: 5 - 用两个栈实现队列.py
# @Project: mianshi
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""
class QueueWithTwoStacks:
    def __init__(self):
        # 初始化两个栈用于push和pop 操作
        self.stack1 =[]
        self.stack2 =[]
    def push(self,value:int)->None:
        # 将元素压入stack1
        self.stack1.append(value)
    def pop(self)->int:
        # 如果stack2为空，则将stack1中的所有元素转移到stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # 如果stack2现在不为空，则弹出最上面的元素
        if self.stack2:
            return self.stack2.pop()
        else:# 反之还是为空说明之前入栈操作存在问题，直接返回-1
            return -1