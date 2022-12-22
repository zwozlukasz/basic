# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 00:44:10 2022

descriptin: how to use range function
"""

def generate_list_from_given_range(start, stop, step):
    return list(range(start, stop, step))


print(generate_list_from_given_range(0, 52, 2))


def generate_range(start, stop, step):
    return range(start, stop, step)

custom_list = list(generate_range(0, 10, 3))
print(custom_list)

custom_list = tuple(generate_range(20, 110, 10))
print(custom_list)


def go_through_the_values(start, stop, step):
    elements = list(range(start, stop, step))
    for element in elements:
        print(element, end=' ')
    return elements
        
go_through_the_values(17, 90, 3)

