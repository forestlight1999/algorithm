#!/usr/bin/env python
# coding=utf-8
'''
@Author: forestlight
@Date: 2019-08-25 09:19:39
@LastEditTime: 2019-09-04 20:33:23
@Description:
'''

import copy
from utils import get_randint_data

class sNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class dNode(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
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

    def bubble_sort(self, style='s'):
        # style : 's' means from smallest to biggest, 'b' means from biggest to smallest
        if self.is_list_empty() or self.head.next == None: return

        """
        index = 0
        # this while loop: taverse index(max traverse time n-1)
        while index < self.list_length - 1:
            p1 = self.head
            current_len = self.list_length - 1 - index
            # this while loop: current disorder link list size
            while current_len > 0:
                if p1.data > p1.next.data: p1.data, p1.next.data = p1.next.data, p1.data
                p1 = p1.next
                current_len -= 1

            index += 1
        """
        p_end = self.end
        while p_end != self.head:
            p1 = self.head
            p_temp = None
            while p1 != p_end:
                p_temp = p1
                if p1.data > p1.next.data:
                    p1.data, p1.next.data = p1.next.data, p1.data
                p1 = p1.next
            p_end = p_temp

        print('list bubble sorted:')

    def merge_sort(self, style='s'):
        def get_mid(head):
            if head == None or head.next == None: return head

            quick = slow = head
            # why we need to judge quick.next.next here?
            #   because quick pointer's step is 2
            while quick.next != None and quick.next.next != None:
                slow = slow.next
                quick = quick.next.next

            print(slow.data)
            return slow

        def merge(head_left, head_right):
            print('merge start:', head_left.data, head_right.data)
            if head_left == None or head_right == None: return None
            left = head_left
            right = head_right

            # 1. define a new head node and merge the half list to new list
            if left.data <= right.data:
                new_head = copy.deepcopy(left)
            else: new_head = copy.deepcopy(right)

            # 2. merge half lists
            temp = copy.deepcopy(new_head)
            count = 0
            while left != None and right != None:
                count += 1
                if count > 10: assert(0)
                if left.data <= right.data:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                print(left, right)
                temp = temp.next

            # 3. merge the left part to new list
            if left != None: temp.next = left
            if right != None: temp.next = right

            print('merge end')
            return new_head

        def sort(head):
            # recursive stop condition
            if self.head == None or self.head.next == None:
                return head
            # recursive algorithm
            left = head
            mid = get_mid(head)
            right = mid.next
            mid.next = None

            return merge(sort(left), sort(right))

        sort(self.head)
        print('list merge sorted:')
        self.display_list()

    def quick_sort(self, style='s'):
        pass

if 1:
    size = 100
    sList = SingleList(size)
    for i in range(10): sList.insert(sNode(get_randint_data()[0]))
    sList.display_list()
    """
    sList.revise()
    node = sList.remove_head()
    print('remove head node:{}{}'.format(node, node.data))
    sList.display_list()
    node = sList.remove_end()
    print('remove end node:{}{}'.format(node, node.data))
    sList.display_list()
    """
    #sList.bubble_sort()
    sList.merge_sort()
    sList.display_list()
