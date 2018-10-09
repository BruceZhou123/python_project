#! /usr/bin/python
#_*_coding=utf-8_*_


def func(name):
    def inner_func(age):
        print 'name', name, 'age', age
    return inner_func

person = func("John")
person(30)
