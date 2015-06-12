#!/usr/bin/env python
# coding:UTF-8

__author__ = 'yuni.net.liberty'

def sort(array):
    unsettled_num = len(array)
    unsettled_final_No = unsettled_num - 1
    while unsettled_final_No > 0:
        for focus in range(0, unsettled_final_No):
            if array[focus] > array[focus + 1]:
                (array[focus], array[focus + 1]) = (array[focus + 1], array[focus])
        unsettled_final_No -= 1


