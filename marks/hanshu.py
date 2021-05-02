#!/usr/bin/env python
# !coding:utf-8

#函数当做变量
def f1():
    return 'hello f1'

per=f1()
print(per)

#函数的参数是函数
def f2(a):
    return  a
print(f2(f1()))

def login(user,psd):
    if user=='hehe' and psd=='000000':
        return 'hahahaha'
    else:
        return 'fild'

def profile(token):
    if token=='hahahaha':
        return 'success'
    else:
        return 'boom!!!!!'

print(profile(login('hehe','000000')))


#函数可以嵌套
def f3():
    def f4():
        return 'hello f4'
    return f4()
print(f3())