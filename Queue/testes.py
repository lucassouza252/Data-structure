# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:24:56 2021

@author: lucas
"""
from myqueue import MyQueue

obj = MyQueue()

obj.queue(1)
obj.queue(2)
obj.queue(3)
obj.queue(4)
obj.queue(5)

obj.to_list()

obj.deque()
obj.deque()

obj.to_list()