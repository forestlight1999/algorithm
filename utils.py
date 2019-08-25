#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def get_randint_data(size=1, _min=-100, _max=100):
    return np.random.randint(_min, _max, size)