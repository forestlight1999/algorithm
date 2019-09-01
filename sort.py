#!/usr/bin/env python
# coding=utf-8
'''
@Author: forestlight
@Date: 2019-08-25 16:29:29
@LastEditTime: 2019-09-01 09:34:22
@Description: implement the classical sort algorithm
'''

from utils import get_randint_data
from collections.abc import Iterable

class Sort(object):
    def __init__(self, cache_len):
        self.cache = [0x0 for i in range(cache_len)]

    '''
    @description: O(n2)/O(n2), O(1), stable
    @param : array; style: 's' means from smallest to biggest, 'b' means from biggest to smallest
    @return: sorted array
    '''
    def bubble_sort(self, array, style='s'):
        assert(isinstance(array, Iterable))

        tep_array = array[:]
        size = len(tep_array)
        if size > 1:
            # this for loop meaning
            #   1. traverse index : for n data, only need n - 1 times traverse
            #   2. current bubble number(also the number of order data till now)
            for ordered_num in range(size - 1):
                is_exchange = False
                # this for loop meaning : current disorder data index range(therefore we need -i
                # why need -1? because for bubble sort, we choose two nearby data for compare
                for dis_index in range(size - 1 - ordered_num):
                    if (style == 's' and tep_array[dis_index] > tep_array[dis_index+1]) or \
                        (style == 'b' and tep_array[dis_index] < tep_array[dis_index+1]):
                        tep_array[dis_index], tep_array[dis_index+1] = tep_array[dis_index+1], tep_array[dis_index]
                        is_exchange = True
                if not is_exchange: break

        print('bubble sorted:{}'.format(tep_array))
        return tep_array

    '''
    @description: O(n2)/O(n2), O(1), stable
    @param {type}
    @return:
    '''
    def select_sort(self, array, style='s'):
        assert(isinstance(array, Iterable))

        # 1. find the smallest or biggest data index from current disorder array
        # 2. switch the found data with current first data of disorder array
        # 3. move disorder start index to the next data and repeat step 1 and 2
        tep_array = array[:]
        size = len(tep_array)
        if size > 1:
            # only need n-1 times to traverse the disorder data(for one data, no need to traverse)
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
    @description: O(n2)/O(n2), O(1), stable
    @param {type}
    @return:
    '''
    def insert_sort(self, array, style='s'):
        assert(isinstance(array, Iterable))
        tep_array = array[:]
        size = len(tep_array)

        if size > 1:
            # 1. this for loop: disorder data sequence start index
            # choose the first data as order sequence
            for dis_index in range(1, size):
                need_insert = tep_array[dis_index]
                # 2. this for loop: order data sequence(reversed)
                for order_index in reversed(range(-1, dis_index)):
                    if tep_array[order_index] > need_insert:
                        tep_array[order_index+1] = tep_array[order_index]
                    else: break
                tep_array[order_index+1] = need_insert

        if style == 'b': tep_array = tep_array[::-1]
        print('insert sorted:{}'.format(tep_array))
        return tep_array

    '''
    @description: O(n1.5)/O(n2), O(1), NOT stable
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
    def merge_sort(self, array, left, right):
        def merge(array, left, right):
            mid = (left + right) // 2
            i = left
            j = mid + 1
            k = left

            # 1. select the smaller item from left array and right array one by one and copy it to cache
            while i <= mid and j <= right:
                if array[i] <= array[j]:
                    self.cache[k] = array[i]
                    i += 1
                else:
                    self.cache[k] = array[j]
                    j += 1
                k += 1
            # 2. copy the rest of array to cache
            while i <= mid:
                self.cache[k] = array[i]
                i += 1
                k += 1
            while j <= right:
                self.cache[k] = array[j]
                j += 1
                k += 1
            # 3. copy cache data to original buffer
            k = left
            while k <= right:
                array[k] = self.cache[k]
                k += 1

        def sort(array, left, right):
            if left < right:
                mid = (left + right) // 2

                sort(array, left, mid)
                sort(array, mid+1, right)
                merge(array, left, right)

        sort(array, left, right)
        print('merge sorted:{}'.format(array))

    '''
    @description:
    @param {type}
    @return:
    '''
    def quick_sort(self, array, left, right):
        def partition(array, left, right):
            i = left # left guard
            j  = right # right guard
            pivot = array[left] # pivot index(choose the left index default)

            while i < j:
                # 1. right guard search the smaller value than pivot first
                while i < j and array[j] >= pivot:
                    j -= 1
                # 2. left guard search the bigger value than pivot then
                while i < j and array[i] <= pivot:
                    i += 1
                # 3. switch the guard's value then
                if i != j: array[i], array[j] = array[j], array[i]

            # 4. switch the pivot's and j's value and return j as new pivot
            array[left], array[j] = array[j], array[left]
            return j

        def sort(array, left, right):
            if left < right:
                pivot = partition(array, left, right)
                sort(array, left, pivot - 1)
                sort(array, pivot + 1, right)

        sort(array, left, right)
        print('quick sorted:{}'.format(array))

    '''
    @description:
    @param {type}
    @return:
    '''
    def count_sort(self, array, style='min'):
        assert(style in ('min', 'max'))
        assert(isinstance(array, Iterable))

        length = len(array)
        if length > 1:
            # 1. traverse array to find max value and min value
            #   if min_val < 0, need to add compensation to nonenegative number
            max_val = max(array)
            min_val = min(array)
            compense = 0 if min_val >= 0 else (-min_val)
            max_val = max_val + compense

            # 2. generate an array to store each value counter
            counter_array = [0x0 for x in range(max_val+1)]
            # 2.1 traverse the original array and store value counter to counter_array
            for item in array:
                # Note: need to add compensation
                counter_array[item + compense] += 1
            # 2.2 add counter_array value one by one to get each value index max index
            for index in range(1, max_val+1):
                counter_array[index] += counter_array[index-1]

            # 3. traverse original array backward and get it index from counter_array
            cache_array = [0x0 for x in range(length)]
            for item in reversed(array):
                cache_array[counter_array[item+compense] - 1] = item
                counter_array[item+compense] -= 1

            # 4. copy cache data to original array
            array = cache_array[:]

        print('court sorted:{}'.format(array))
        return array

if 1:
    size = 10
    sort = Sort(size)
    array = get_randint_data(size)
    sort.bubble_sort(array)
    array = get_randint_data(size)
    sort.select_sort(array)
    array = get_randint_data(size)
    sort.insert_sort(array)
    array = get_randint_data(size)
    sort.hell_sort(array)
    array = get_randint_data(size)
    sort.merge_sort(array, 0, size - 1)
    array = get_randint_data(size)
    sort.quick_sort(array, 0, size - 1)
    array = get_randint_data(size)
    sort.count_sort(array)



