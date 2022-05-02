#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022
#Generates random .csv file used for importing graph data

from random import random,randint  #for random graph on every instance

def generate_files():
    #dictionary for mapping number to alphabet character
    num_map = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

     # designates and generates graph with random # of nodes
    num_nodes = randint(5,25)

    #tracker to ensure every node has an edge
    tracker= []

    for node in range(0, num_nodes):
        tracker.append(node)

    #exits when every node gets an edge
    while len(tracker) > 0:
        #picks two different edges
        edge1 = randint(0,num_nodes - 2)
        edge2 = randint(edge1 + 1, num_nodes - 1)
        #generates unique chance to fail
        fail_chance = randint(0,10)
        
        #ensures every node gets an edge
        if edge1 in tracker:
            tracker.remove(edge1)
        if edge2 in tracker:
            tracker.remove(edge2)

        #populates graph with fixed values
        graph.add_edge(edge1, edge2, fail_chance)
