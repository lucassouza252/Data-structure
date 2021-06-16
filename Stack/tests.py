# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:46:51 2021

@author: lucas
"""
from mystack import MyStack

obj = MyStack()

obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)

obj.to_list()

obj.pop()
obj.pop()

obj.to_list()
