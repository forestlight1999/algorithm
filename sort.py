#!/usr/bin/env python
# coding=utf-8
'''
@Author: forestlight
@Date: 2019-08-25 16:29:29
@LastEditTime: 2019-08-25 21:27:47
@Description: implement the classical sort algorithm
'''

from utils import get_randint_data
from collections.abc import Iterable

class Sort(object):
    def __init__(self):
        pass

    '''
    @description: bubble sort
    @param : array; style: 's' means from smallest to biggest, 'b' means from biggest to smallest
    @return: sorted array
    '''
    def bubble_sort(self, array, style='s'):
        assert(isinstance(array, Iterable))

        tep_array = array[:]
        size = len(tep_array)
        if size > 1:
            for ordered_num in range(size):
                is_exchange = False
                for dis_index in range(size - 1 - ordered_num):
                    if (style == 's' and tep_array[dis_index] > tep_array[dis_index+1]) or \
                        (style == 'b' and tep_array[dis_index] < tep_array[dis_index+1]):
                        tep_array[dis_index], tep_array[dis_index+1] = tep_array[dis_index+1], tep_array[dis_index]
                        is_exchange = True
                if not is_exchange: break

        print('bubble sorted:{}'.format(tep_array))
        return tep_array

    '''
    @description:
    @param {type}
    @return:
    '''
    def select_sort(self, array, style='s'):
        assert(isinstance(array, Iterable))

        tep_array = array[:]
        size = len(tep_array)
        if size > 1:
            # if only 2 item left, just sort one time
            for disorder_start in range(size - 1) :
                min_index = disorder_start
                for disorder_index in range(disorder_start, size):
                    if style == 's' and tep_array[disorder_index] < tep_array[min_index] or \
                        style == 'b' and tep_array[disorder_index] > tep_array[min_index]:
                        min_index = disorder_index
                if min_index != disorder_start:
                    tep_array[disorder_start], tep_array[min_index] = tep_array[min_index], tep_array[disorder_start]

        print('select sorted:{}'.format(tep_array))
        return tep_array

    '''
    @description:
    @param {type}
    @return:
    '''
    def insert_sort(self, array, style='s'):
        assert(isinstance(array, Iterable))
        tep_array = array[:]
        size = len(tep_array)

        if size > 1:
            for dis_index in range(1, size):
                need_insert = tep_array[dis_index]
                for order_index in reversed(range(-1, dis_index)):
                    if tep_array[order_index] > need_insert:
                        tep_array[order_index+1] = tep_array[order_index]
                    else: break
                tep_array[order_index+1] = need_insert

        if style == 'b': tep_array = tep_array[::-1]
        print('insert sorted:{}'.format(tep_array))
        return tep_array

    '''
    @description:
    @param {type}
    @return:
    '''
    def hell_sort(self, array, style='s'):
        assert(isinstance(array, Iterable))
        tep_array = array[:]
        size = len(tep_array)

        # hell sort is narrow down the gap of insert sort
        if size > 1:
            gap = size // 2
            while gap > 0:
                dis_index = gap
                while dis_index < size:
                    need_insert = tep_array[dis_index]

                    order_index = dis_index - gap
                    while order_index >= 0 and tep_array[order_index] > need_insert:
                        tep_array[order_index+gap] = tep_array[order_index]
                        order_index -= gap

                    tep_array[order_index+gap] = need_insert

                    dis_index += 1

                gap = gap // 2

        if style == 'b': tep_array = tep_array[::-1]
        print('hell sorted:{}'.format(tep_array))
        return tep_array


    '''
    @description:
    @param {type}
    @return:
    '''
    def merge_sort(self, array, style='s'):
        pass

    '''
    @description:
    @param {type}
    @return:
    '''
    def quick_sort(self, array, style='s'):
        pass

if 1:
    sort = Sort()
    array = get_randint_data(10)
    sort.bubble_sort(array)
    array = get_randint_data(10)
    sort.select_sort(array)
    array = get_randint_data(10)
    sort.insert_sort(array)
    array = get_randint_data(10)
    sort.hell_sort(array)


