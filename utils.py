#!/usr/bin/env python
# coding=utf-8
"""
@Author: forestlight
@Date: 2019-08-25 11:06:10
@LastEditTime: 2019-09-01 09:34:18
@Description:
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

def get_randint_data(size=1, _min=0, _max=100):
    array = list(np.random.randint(_min, _max, size))
    # print("random data:{}".format(array))
    pprint("Generate random int data:{}".format(array))

    return array


def create_graph(gg, node, pos=None, x=0, y=0, layer=1):
    if pos is None:
        pos = {}
    pos[node.data] = (x, y)
    if node.left:
        gg.add_edge(node.data, node.left.data)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(gg, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        gg.add_edge(node.data, node.right.data)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(gg, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return gg, pos


def draw_tree(node):
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()
