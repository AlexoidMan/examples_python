import sys
# sys.path.append("/home/alex/PycharmProjects/pythonProject/patterns/") # Works Ok
# sys.path.insert(0, 'patterns/')

# import os, sys
# from os.path import dirname, join, abspath
# sys.path.insert(0, abspath(join(dirname(__file__), 'patterns/')))

from patterns.singleton import *
import metaclasses

# import abstract_class as abstract
# import namedtuple as nt

# import my_decorator
# import shallowDeep_copy as copyTest

import data_structures as datas
# import data_structures2 as datas2

# import looping_iteration
import iterators_generator
import classVSinstance
import dict_tricks
#
# print(my_decorator.greet())
#
# print(f'{my_decorator.say("Lane", "Hello World!")}')
#
# print(f'{my_decorator.say.__doc__} + " " + {my_decorator.say.__name__}')
#
# my_decorator.greet_pure = my_decorator.strong(my_decorator.greet_pure)  # apply decorator directly: greet = strong(greet)  - greet now has the decorator
# print(f'{my_decorator.greet_pure()}')
# # print(my_decorator.strong(my_decorator.greet_pure))
#
#
# ''' Testing shallow and deep copy '''
# # copyTest.copy_testing()
#
# #function is an object
# b = copyTest.copy_testing
# b()

# ''' Testing abstract classes '''
# abstract.test_abstract()

# ''' Testing named tuples '''
# nt.test_namedtuple()


'''Test class, instance, static methods '''
# classVSinstance.test_classVSinstance()

'''Test data structures'''
# datas.test_namedtuple()

'''Test data structures 2'''
# datas2.test_datastructs()

'''Test loop and iteration'''
# looping_iteration.test_loop_iteration()
# looping_iteration.test_comprehensions()
# looping_iteration.test_list_slicing()
# looping_iteration.test_iterators()

# iterators_generator.test_iterators()

''' Test patterns'''
# testing_Singleton()

''' Test metaclasses '''
# metaclasses.test_metaclasses()

''' Test Dict Tricks '''
dict_tricks.test_Dict_tricks()