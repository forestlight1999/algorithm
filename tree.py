#!/usr/bin/env python
# coding=utf-8
'''
@Author: forestlight
@Date: 2019-08-31 18:03:30
@LastEditTime: 2019-09-01 08:50:44
@LastEditors:
@Description: implement the tree related algorithm
'''

from utils import get_randint_data
from collections.abc import Iterable

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, array, size):
        assert(isinstance(array, Iterable))
        assert(size == len(array))
        self.size = size
        self.cache = [0x0 for x in range(size)]

    def build_tree(self, array):
        # use recursive algorithm to generate binary tree
        pass

    def preorder_traver(self):
        pass

    def inorder_traver(self):
        pass

    def postorder_traver(self):
        pass