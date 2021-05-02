#!/usr/bin/env python
# !coding:utf-8

#装饰器：在一个函数上添加@+函数名。被装饰函数是装饰函数的参数

def getmsg(fanc):
    def inner():
        print('hello getmsg')
        fanc()
    return inner

@getmsg
def f1():
    print('hello f1')

@getmsg
def f2():
    print('hello f2')

f1()
f2()

