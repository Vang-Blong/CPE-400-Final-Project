#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022
#Graph class

class Graph:

    def __init__(self, edges):
        self.edge = edges
        self.graph = []

    def add_edge(self, node1, node2, fail_chance, score):
        self.graph.append([node1,node2, fail_chance, score])

