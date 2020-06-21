#!/usr/bin/env python
# coding=utf-8
"""
@Author: forestlight
@Date: 2019-08-31 18:03:30
@LastEditTime: 2019-09-04 20:34:29
@LastEditors:
@Description: implement the tree related algorithm
"""
from utils import draw_tree, get_randint_data
from collections.abc import Iterable
from enum import IntEnum


def bpp(node=None, _end_=', '):
    if node and isinstance(node, Node):
        print(node.data, end=_end_)
    elif isinstance(node, str):
        print(node, end=_end_)


class TraverType(IntEnum):
    recurse = 0,
    stack = 1,


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, data=None):
        # data must be iterable, ex: list/tuple, etc
        self.data_list = data
        self.root = None
        self.create(0)

    # use recursive method to create the binary tree
    def create(self, node, index=0):
        if self.data_list:
            if index < len(self.data_list):
                node = Node(self.data_list[index])
                if index == 0:
                    self.root = node

                node.left = self.create(node.left, 2 * index + 1)
                node.right = self.create(node.right, 2 * index + 2)
                return node
            else:
                return None

    """
    traverse the binary tree
    """
    @staticmethod
    def preorder_travel(node, mode=TraverType.recurse):
        def preorder_recurse(node):
            if node:
                bpp(node)
                preorder_recurse(node.left)
                preorder_recurse(node.right)

        if mode == TraverType.recurse:
            bpp("\nPre-Traverse[recursive]:", _end_=' ')
            preorder_recurse(node)
        elif mode == TraverType.stack:
            bpp("\nPre-Traverse[non-recur]:", _end_=' ')

            """
            why need to check node first ?
                1) you should check the null node first
                2) you need to enter the outside while loop first because the stack if empty @begaining
            why need to check the stack length ?
                because if the stack(list) is empty, you have already finish the traverse
            """
            stack = []
            while node or len(stack):
                # search node sequence : left -> mid -> right
                # preorder : mid(print the value) -> left -> right
                while node:
                    # print the mid node, push it into stack(because it has not finish the traverse)
                    bpp(node)
                    stack.append(node)
                    node = node.left

                if len(stack):
                    node = stack.pop()
                    node = node.right

    @staticmethod
    def inorder_travel(node, mode=TraverType.recurse):
        def inorder_recurse(node):
            if node:
                inorder_recurse(node.left)
                bpp(node)
                inorder_recurse(node.right)

        if mode == TraverType.recurse:
            bpp("\nIn-Traverse[recursive]:", _end_=' ')
            inorder_recurse(node)
        elif mode == TraverType.stack:
            bpp("\nIn-Traverse[non-recur]:", _end_=' ')

            stack = []
            while node or len(stack):
                while node:
                    stack.append(node)
                    node = node.left

                if len(stack):
                    node = stack.pop()
                    bpp(node)
                    node = node.right

    @staticmethod
    def postorder_travel(node, mode=TraverType.recurse):
        def post_recurse(node):
            if node:
                post_recurse(node.left)
                post_recurse(node.right)
                bpp(node)

        if mode == TraverType.recurse:
            bpp("\nPost-Traverse[recursive]:", _end_=' ')
            post_recurse(node)
        else:
            bpp("\nPost-Traverse[non-recur]:", _end_=' ')

            stack = []
            last_traver = None
            """
            when to print the mid node data ?
                1) if the node is leaf node
                2) if the right node of current node has been traversed before
            """
            while node or len(stack):
                while node:
                    stack.append(node)
                    node = node.left

                if len(stack):
                    node = stack.pop()
                    # if current node is leaf node or its right node has been traverse before, print it
                    if not node.right or last_traver == node.right:
                        bpp(node)
                        # need to set the last_traver here
                        last_traver = node
                        # why set node to none here? => because we should not find its left tree any more
                        node = None
                    else:
                        # right node has not been traverse, need to push the node again and search the right tree then
                        stack.append(node)
                        node = node.right

    @staticmethod
    def breadth_travel(node):
        if not node:
            return

        bpp("\nBreadth-Traverse[recursive]:", _end_=' ')
        queue = [node,]
        while len(queue):
            # pop the first node of the queue
            node = queue.pop(0)
            bpp(node)
            # enqueue the left and right node of current node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def find(self, data, node):
        # use traverse algorithm to find the node
        if node:
            if node.data == data:
                print('find the node', node)
                return node
            else:
                self.find(data, node.left)
                self.find(data, node.right)
        return None


class BinarySearchTree(BinaryTree):
    def __init__(self, seq=()):
        super().__init__()
        assert isinstance(seq, Iterable)
        self.root = None
        # use variable parameter to generate binary tree
        # default use first item as root node
        self.create(*seq)

    def create(self, *seq):
        if not seq:
            return

        # use the first data as the root
        if not self.root:
            self.root = Node(seq[0])
            seq = seq[1:]
        # insert variables into current tree
        if len(seq):
            for item in seq:
                node = self.root
                while True:
                    if item > node.data:
                        if not node.right:
                            node.right = Node(item)
                            break
                        else:
                            node = node.right
                    else:
                        if not node.left:
                            node.left = Node(item)
                            break
                        else:
                            node = node.left

    def find(self, data):
        pass


class BinaryHeap(BinaryTree):
    pass


rand_data = get_randint_data(16)
# if 1:
#     bst = BinarySearchTree([9,8,3,5,2,6,11,13,7,1,4])
#     bst.preorder_traverse(bst.root)
#     print('\n')
#     bst.inorder_traverse(bst.root)
#     print('\n')
#     bst.postorder_traverse(bst.root)
#     print('\n')
#     draw(bst.root)
if 1:
    bi_tree = BinaryTree(rand_data)
    root_node = bi_tree.root
    bi_tree.preorder_travel(root_node)
    bi_tree.preorder_travel(root_node, TraverType.stack)

    bi_tree.inorder_travel(root_node)
    bi_tree.inorder_travel(root_node, TraverType.stack)

    bi_tree.postorder_travel(root_node)
    bi_tree.postorder_travel(root_node, TraverType.stack)

    bi_tree.breadth_travel(root_node)
    draw_tree(bi_tree.root)
    # bi_tree.find(3, bi_tree.root)
