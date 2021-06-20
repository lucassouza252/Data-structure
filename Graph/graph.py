# -*- coding: utf-8 -*-
class Graph:
    
    def __init__(self):
        self.vertex = []
    
    def add_vertex(self, vert):
        self.vertex.append(vert)
    
    def show_graph(self):
        for x in self.vertex:
            x.show_neighbors()