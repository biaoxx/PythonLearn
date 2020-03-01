#!/bin/pythons
# coding=utf-8



ls = [1,2,3]


"""
 对象通过调用next方法，获取值
"""
myIter = iter(ls)
i = myIter.__next__()
print(i)
i = myIter.__next__()
print(i)
i = myIter.__next__()
print(i)


"""
类中实现迭代。

迭代器通过 StopIteration标识 完成
"""
class MyIter2(object):
    def  __init__(self,ls):
        self.ls = ls
        self.index = 0

    def __next__(self):
        if (self.index >= len(self.ls)):
             raise  StopIteration  # 迭代器通过 StopIteration标识 完成
        tmp = self.ls[self.index]
        self.index+=1

        return tmp

    def __iter__(self):   # 包含下一个状态的对象， 这个对象会调用__next__方法获取值
        return self

myIter = MyIter2(ls)
for i in iter(myIter):
    print(i)



