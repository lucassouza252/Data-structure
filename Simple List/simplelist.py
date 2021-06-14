# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:20:08 2021

@author: lucas
"""
from node import Node

class SimpleList:
    
    current = None
    _next = None
    first = None
    
    def add(self, data):
        """
        Description: Add new data in list.
        
        Parameters
        ----------
        data: Any Value.

        Returns
        -------
        None.
        """
        if self.first == None:
            new_node = Node(data)
            new_node.next = None
            self.first = new_node
            self.current = new_node
            
        else:
            new_node = Node(data)
            self.current.next = new_node
            self.current = new_node
    
    def isin(self, data):
        """
        Description: Check if data is in list.
        
        Parameters
        ----------
        data: Any Value.

        Returns
        -------
        bool: If value in list, returns True, else, returns False;
        """
        aux = self.first
        
        while aux is not None:
            if aux.data == data:
                return True
            aux = aux.next
        return False
    
    def to_list(self):
        """
        Description: Print all values in list
            
        Parameters
        ----------
        None
        
        Returns
        -------
        None.
        """
        aux = self.first
        
        while aux is not None:
            print("[{}]".format(aux.data))
            aux = aux.next
    
        