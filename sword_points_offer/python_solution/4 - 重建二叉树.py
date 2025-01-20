#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/1/14 0014 10:54
# @Author: Administrator
# @File: 4 - 重建二叉树.py
# @Project: mianshi
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
一、问题解析：
（1）前序遍历：
前序遍历的顺序是：根节点 -> 左子树 -> 右子树。
前序遍历的第一个节点一定是二叉树的根节点。
（2）中序遍历：
中序遍历的顺序是：左子树 -> 根节点 -> 右子树。
在中序遍历中，根节点的左边是左子树的所有节点，右边是右子树的所有节点。
二、重建二叉树的思路：
通过前序遍历找到根节点。
在中序遍历中找到根节点的位置，从而确定左子树和右子树的节点范围。
递归地重建左子树和右子树。
示例解析
假设输入的前序遍历和中序遍历分别为：

前序遍历：[1, 2, 4, 7, 3, 5, 6, 8]

中序遍历：[4, 7, 2, 1, 5, 3, 8, 6]

步骤：
根节点：
前序遍历的第一个节点是 1，所以根节点的值为 1。
在中序遍历中找到 1 的位置，左边 [4, 7, 2] 是左子树，右边 [5, 3, 8, 6] 是右子树。
左子树：
前序遍历中左子树的部分是 [2, 4, 7]。
中序遍历中左子树的部分是 [4, 7, 2]。
递归构建左子树。
右子树：
前序遍历中右子树的部分是 [3, 5, 6, 8]。
中序遍历中右子树的部分是 [5, 3, 8, 6]。
递归构建右子树。
递归终止：
当子树为空时，返回 None。
"""
from typing import List
class TreeNode: # 构建数结构
    def __init__(self,val=0,left=None,right=None):
        self.val = val # 数节点
        self.left = left # 左子树
        self.right = right # 右子树
class Solution:
    def buildTree(self,preorder:List[int],inorder:List[int])->TreeNode:
        if not preorder or not inorder:
            return None
        root_val = preorder[0] # 根节点
        root=TreeNode(root_val) # 建立树
        mid_idx = inorder.index(root_val) # 获取在中序遍历中根节点的下标
        # preorder[1:mid_idx + 1] 表示从前序排列中从第二个数字起，mid_idx+1代表有这些数据作为左子树，:mid_idx代表有右子树数据
        root.left=self.buildTree(preorder[1:mid_idx+1],inorder[:mid_idx])
        root.right=self.buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
        return root


