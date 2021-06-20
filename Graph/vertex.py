# -*- coding: utf-8 -*-
class Vertex:
    
    def __init__(self, data):
        self.neighbors = []
        self.vertex = data
        
    def add_neighbor(self, data):
        self.neighbors.append(data)
    
    def show_neighbors(self):
        print(self.neighbors)