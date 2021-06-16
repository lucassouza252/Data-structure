# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:32:12 2021

@author: lucas
"""
from node import Node

class MyStack:
    first = None
    current = None
    
    def push(self, data):
        """
        Parameters
        ----------
        data: Any Value.

        Returns
        -------
        None.
        """
        new_node = Node(data)
        if self.first == None:
            self.first = new_node
            self.current = self.first
        else:
            self.current.next = new_node
            new_node.previous = self.current
            self.current = new_node
    
    def pop(self):
        """
        Returns
        -------
        data: Any Value Saved Before
        """
        data = self.current.data
        self.current = self.current.previous
        self.current.next = None
        return data
    
    def to_list(self):
        """
        Description: Print all elements in stack.
        Returns
        -------
        None.
        """
        aux = self.first
        
        while aux is not None:
            print("[{}]".format(aux.data))
            aux = aux.next