#!/usr/bin/env python
# coding=utf-8
'''
@Author: forestlight
@Date: 2019-08-25 11:06:10
@LastEditTime: 2019-08-25 18:00:39
@Description:
'''
import numpy as np

def get_randint_data(size=1, _min=-100, _max=100):
    array =  np.random.randint(_min, _max, size)
    print("random data:{}".format(array))

    return array