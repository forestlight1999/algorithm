#!/usr/bin/env python
# coding=utf-8
'''
@Author: forestlight
@Date: 2019-08-25 09:19:39
@LastEditTime: 2019-08-25 18:00:34
@Description:
'''

from utils import get_randint_data

class sNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleList(object):
    def __init__(self, max_size = 1000):
        self.head = None
        self.end = None
        self.list_length = 0
        self.list_max_size = max_size


    def is_list_empty(self): return (self.head == None)

    def is_list_full(self): return (self.list_length >= self.list_max_size)

    def get_list_size(self): return self.list_length, self.list_max_size

    def display_list(self):
        if self.is_list_empty(): print('Sigle list is empty')
        else:
            node = self.head
            while node:
                print('{}'.format(node.data), end=' ')
                node = node.next
            print('\n')

    """
    'b' means to insert at the beginning of the list, 'e' means to insert at the end of the list
    """
    def insert(self, new_node, insert_pos='e'):
        if not new_node or self.is_list_full(): return False
        assert(isinstance(new_node, sNode))

        if self.is_list_empty():
            self.head = self.end = new_node
        else:
            assert(insert_pos in ('b', 'e'))
            if insert_pos == 'e':
                assert(self.end)
                self.end.next = new_node
                self.end = new_node
            elif insert_pos == 'b':
                new_node.next = self.head
                self.head = new_node
            else:
                print("wrong insert pos parameter:{0}, must 'b' or 'e'".format(insert_pos))
                return False

        self.list_length += 1
        return True

    def insert_head(self, new_node):
        return self.insert(new_node, 'b')

    def insert_end(self, new_node):
        return self.insert(new_node, 'e')

    """
    node: defaule is None
    if node is None
        pos is 'b': remove first node
        pos is 'e': remove last node
    """
    def remove(self, node=None, pos='b'):
        if self.is_list_empty():
            print ('List is empty')
            return None

        # if there is just one item in list
        if not self.head.next:
            if self.head == node or not node:
                node = self.head
                self.head = self.end = None
                self.list_length -= 1
        else:
            if not node:
                assert(pos in ('b', 'e'))
                if pos == 'b':
                    # remove the first node
                    node = self.head
                    self.head = self.head.next
                else:
                    # remove the last node
                    tep_node = self.head
                    node = self.end
                    while tep_node:
                        if tep_node.next == self.end:
                            self.end = tep_node
                            tep_node.next = None
                            break
                        tep_node = tep_node.next

                self.list_length -= 1
            else:
                # remove any node on the list
                p1_node = self.head
                p2_node = p1_node.next

                while p2_node:
                    if p2_node == node:
                        self.list_length -= 1
                        if p2_node == self.end: self.end = p1_node
                        p1_node.next = p2_node.next
                    else: p1_node,p2_node = p2_node,p1_node

            return node

    def remove_head(self): return self.remove(None, 'b')

    def remove_end(self): return self.remove(None, 'e')

    def revise(self):
        if self.is_list_empty() or self.head.next == None: return
        else:
            p1_node = self.head
            p2_node = p1_node.next
            # p3 node is just used to record p2_node next node`
            p3_node = None

            while p2_node:
                p3_node = p2_node.next
                p2_node.next = p1_node
                p1_node,p2_node,p3_node = p2_node,p3_node,None

            self.head, self.end = self.end, self.head
            self.end.next = None

        self.display_list()

if 1:
    size = 100
    sList = SingleList(size)
    for i in range(10): sList.insert(sNode(get_randint_data()[0]))
    sList.display_list()
    sList.revise()
    node = sList.remove_head()
    print('remove head node:{}{}'.format(node, node.data))
    sList.display_list()
    node = sList.remove_end()
    print('remove end node:{}{}'.format(node, node.data))
    sList.display_list()