#!/usr/bin/env python
# coding=utf-8
'''
@Author: forestlight
@Date: 2019-08-25 17:06:29
@LastEditTime: 2019-08-27 22:22:58
@Description: used to implement the heap data structure
'''
from utils import get_randint_data
from collections.abc import Iterable

'''
@description: now we use array to implement min heap
@param {type}
@return:
'''
class Heap(object):
    def __init__(self, array, size):
        assert(isinstance(array, Iterable))
        assert(size > 0 and len(array) == size)

        # the array is random data array
        self.heap_size = size
        self.array = array

    '''
    @description: use sink API to generate heap
    @param: style: min(min heap) / max(max heap)
    @return:
    '''
    def generate_heap(self, heap_size, style='min'):
        # now we use sink API to generate min heap
        # 1. get the last none-leaf node index: heap_size / 2
        index = heap_size // 2
        while index >= 0:
            self.sink(index, heap_size, style)
            index -= 1

        print('generate {} heap: {}'.format(style, self.array))

    '''
    @description: assume that we still storage the rist element of the array
                  parent_index i: left_child_index(2*i+1), right_child_index(2*i+2)
                  child_index i: parent_index((i-1)/2)
                  left_child_index i: right_child_index = left_child_index + 1
    @param: min(min heap)/max(max heap)
    @return:
    '''
    def rise(self, index, heap_size, style='min'):
        # default rise the last data of array(new data will be appened to end of array)
        assert(0 <= index < heap_size)
        assert(style in ('min', 'max'))

        array = self.array
        child_index = index
        parent_index = (child_index - 1) // 2

        value = array[index]

        while parent_index >= 0:
            if (style == 'min' and array[parent_index] > value) or \
                    (style == 'max' and array[parent_index] < value):
                array[child_index] = array[parent_index]
                child_index = parent_index
                parent_index = (parent_index - 1) // 2
            else:
                array[child_index] = value
                break

    '''
    @description:
    @param {type}
    @return:
    '''
    def sink(self, index, heap_size, style='min'):
        assert(0 <= index < heap_size)
        array = self.array
        parent_index = index
        child_index = 2 * parent_index + 1
        value = array[index]

        while child_index < heap_size:
            min_child = min(array[child_index], array[child_index+1]) if child_index + 1 < heap_size else array[child_index]
            max_child = max(array[child_index], array[child_index+1]) if child_index + 1 < heap_size else array[child_index]

            # 1. check whether parent child has already arrive the right position
            if (style == 'min' and value <= min_child) or \
                    (style == 'max' and value >= max_child):
                array[parent_index] = value
                break

            # 2. update parent_index and child_index
            array[parent_index] = array[child_index]
            parent_index = child_index
            child_index = 2 * child_index + 1

    '''
    @description: sort the array through binary heap
    @param: 's': sort array data from smallest to biggest, need to generate max heap first
            'b': sort array data from biggest to smallest, need to generate min heap first
    @return:
    '''
    def sort(self, style='s'):
        assert(style in ('s', 'b'))
        array = self.array
        heap_size = self.heap_size

        # 1. generate the heap first
        if style == 's': self.generate_heap(heap_size, 'max')
        else: self.generate_heap(heap_size, 'min')

        # 2. use sink API to sort the array
        current_size = heap_size - 1
        while current_size > 1:
            # 2.1 switch top node and current last node
            array[0], array[current_size-1] = array[current_size-1], array[0]
            # 2.2 reduce current heap size
            current_size -= 1
            # 2.3 sink the top node
            self.sink(0, current_size)

        print('heap sorted: {}'.format(array))


if 1:
    size = 3
    array = get_randint_data(size)
    heap = Heap(array, size)
    heap.sort('s')

