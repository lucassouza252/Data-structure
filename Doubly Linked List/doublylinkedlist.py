# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:16:19 2021

@author: lucas
"""
from node import Node

class DoublyLinkedList:
    
    current = None
    first = None
    
    def add(self, data):
        """
        Description: Add data in the list and configure before and after.
        
        Parameters
        ----------
        data : Any Value.

        Returns
        -------
        None.

        """
        new_data = Node(data)
        
        if self.first == None:
            self.first = new_data
            self.current = self.first
        else:
            self.current.next = new_data
            new_data.previous = self.current
            self.current = new_data
    
    def to_list(self):
        """
        Description: Print all values of the list.
        
        Returns
        -------
        None.

        """
        aux = self.first
        while aux is not None:
            print("Before: {}, Next: {}, Data: {}".format(aux.previous, aux.next, 
                                                          aux.data))
            aux = aux.next