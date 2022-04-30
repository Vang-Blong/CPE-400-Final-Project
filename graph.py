#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022

#Graph class
class Graph:

    #build graph and number of nodes
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = []
    
    #connects nodes and adds edge properties
    #fail chance = random value 1-100 of node to fail
    #score = defaults to 50, will dynamically attempt to calculate fail chance over time
    def add_edge(self, node1, node2, fail_chance, score=50):
        self.graph.append([node1,node2, fail_chance, score])

