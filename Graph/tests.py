# -*- coding: utf-8 -*-
from vertex import Vertex
from graph import Graph


obj = Graph()

vert_a = Vertex("A")
vert_a.add_neighbor("B")

vert_b = Vertex("B")
vert_b.add_neighbor("C")
vert_b.add_neighbor("D")

vert_c = Vertex("C")
vert_c.add_neighbor("B")
vert_c.add_neighbor("E")

vert_d = Vertex("D")
vert_d.add_neighbor("A")

vert_e = Vertex("E")
vert_e.add_neighbor("B")

obj.add_vertex(vert_a)
obj.add_vertex(vert_b)
obj.add_vertex(vert_c)
obj.add_vertex(vert_d)
obj.add_vertex(vert_e)

obj.show_graph()