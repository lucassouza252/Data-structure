# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:20:38 2021

@author: lucas
"""
from node import Node

class MyQueue:
    
    first = None
    current = None
    
    def queue(self, data):
        new_node = Node(data)
        
        if self.first == None:
            self.first = new_node
            self.current = self.first
        else:
            self.current.next = new_node
            self.current = new_node
    
    def deque(self):
        data = self.first.data
        self.first = self.first.next
        return data
    
    def to_list(self):
        aux = self.first
        
        while aux is not None:
            print("[{}]".format(aux.data))
            aux = aux.next