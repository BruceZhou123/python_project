#! /usr/bin/python
#coding=utf-8

def fun1(name, age):
	print name
	print age
	return

fun1("John", 18)

print "#" * 50

def fun2(name, age):
	print name
	print age
	return

fun2( age =20, name="zhangsan")

print "#" * 50

def fun3(name, age =30):
	print name
	print age
	return

fun3("lisi")

print "#" * 50

def fun4(name, age, *c):
	print name
	print age
	print c
	return

fun4("wangwu", 40, "hello", 45, 3.14)