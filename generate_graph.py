#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022
#Generates random graph file

from sys import path
path.append(".")
from graph import Graph  #imports graph class
from random import random,randint  #for random graph on every instance

def generate_graph():
    
    # designates and generates graph with random # of nodes
    num_nodes = randint(8,12)
    graph = Graph(num_nodes)

    #tracker to ensure every node has an edge
    tracker= []

    for node in range(1, num_nodes):
        tracker.append(node)

    while len(tracker) > 0:
        #picks two different edges
        edge1 = randint(1,num_nodes - 2)
        edge2 = randint(edge1 + 1, num_nodes)
        #generates unique chance to fail
        fail_chance = randint(0,10)
        
        #ensures every node gets an edge
        if edge1 in tracker:
            tracker.remove(edge1)
        if edge2 in tracker:
            tracker.remove(edge2)

        #populates graph with fixed values
        graph.add_edge(edge1, edge2, fail_chance)

    graph.bellman_ford(2)
    #removes redundant graph objects
    

generate_graph()
#def __init__():
#    generate_graph()