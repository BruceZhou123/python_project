#!/usr/bin/python
#_*_coding=utf-8_*_
# hi()-->printTime(hi)-->wrappendfunc()-->hi()


from time import ctime


def printTime(func):
    def wrappendfunc():
        print "The func name is %s" % (func.__name__)
        print "The time is %s" % (ctime())
        return func()
    return wrappendfunc


@printTime
def hi():
    print "hi ,world!"

hi()
