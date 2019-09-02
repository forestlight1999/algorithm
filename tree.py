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
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.data] = (x, y)
    if node.left:
        G.add_edge(node.data, node.left.data)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.data, node.right.data)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)

def draw(node):
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, data=None):
        # data must be iterable, ex: list/tuple, etc
        assert isinstance(data, Iterable)
        self.data_list = data
        self.root = None
        self.create(0)
    
    # use recursive method to create the binary tree
    def create(self, node, index=0):
        if self.data_list:
            if index < len(self.data_list):
                node = Node(self.data_list[index])
                if index == 0: self.root = node
                
                node.left = self.create(node.left, 2 * index + 1)
                node.right = self.create(node.right, 2 * index + 2)
                return node
            else: return None

    """
    tranverse the binary tree
    """
    def preorder_traverse(self, node):
        if node:
            print(node.data, end=', ')
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)

    def inorder_traverse(self, node):
        if node:
            self.inorder_traverse(node.left)
            print(node.data, end=', ')
            self.inorder_traverse(node.right)

    def postorder_traverse(self, node):
        if node:
            self.postorder_traverse(node.left)
            self.postorder_traverse(node.right)
            print(node.data, end=', ')

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

class BalBinaryTree(BinaryTree):
    def __init__(self, seq=()):
        assert isinstance(seq, Iterable)
        self.root = None
        # use variable parameter to generate binary tree
        # default use first item as root node
        self.create(*seq)

    def create(self, *seq):
        if not seq: return
        
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
                        else: node = node.right
                    else:
                        if not node.left:
                            node.left = Node(item)
                            break
                        else: node = node.left
    
    def find(self, data):
        pass
    
class BinaryHeap(BinaryTree):
    pass

if 0:
    ba_tree = BalBinaryTree([9,8,3,5,2,6,11,13,7,1,4])
    ba_tree.preorder_traverse(ba_tree.root)
    print('\n')
    ba_tree.inorder_traverse(ba_tree.root)
    print('\n')
    ba_tree.postorder_traverse(ba_tree.root)
    print('\n')
    draw(ba_tree.root)
if 1:
    bi_tree = BinaryTree([9,8,3,5,2,6,11,13])
    #bi_tree.preorder_traverse(bi_tree.root)
    #draw(bi_tree.root)
    bi_tree.find(3, bi_tree.root)
