#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function


def divide_vector(n, m):
    '''
        The function divides vector of size n on blocks of size m.
        
        Input:
        n : Integer, size of vector
        m : Integer, size of block
        Output:
        List of pairs (begin_index, end_index)
    '''
    
    block_size = n // m
    first_block_size = block_size
    if n % m:
        first_block_size = n % m // 2
    begin_index = 0
    end_index = max(0, first_block_size - 1)
    blocks_count = m
    indexes_list = []
    if n % m == 1:
        blocks_count += 1
    elif n % m > 1:
        blocks_count += 2
    for i in range(blocks_count):
        print('begin index {0}, end index {1}'.format(begin_index, end_index))
        indexes_list.append((begin_index, end_index))
        begin_index = end_index + 1
        end_index = min(begin_index + block_size, n) - 1
    return indexes_list


divide_vector(13, 3)
