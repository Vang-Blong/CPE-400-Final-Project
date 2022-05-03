#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022
#Imports graph data and visualizes it using matplotlib

import generate_files #for simulating a new graph in each instance
import networkx as nx  #for graph data structur and network analysis features
import matplotlib.pyplot as plt #for visualization
import cv2 #matplotlib dependency
import numpy #additional analysis
from random import randint # for random number generation

#import filedata
def get_data(filename):
    #opens .csv files, reads line by line
    with open(filename, "r", encoding="utf8") as input:
        lines = input.read().split("\n")
        data = [line.split(",") for line in lines]
        head = data[0]
        tail = data[1:]
    #returns header info and the remaining actual data as a tail
    return head, tail[:-1]

#run graph and visualize it
def fault_routing():
    #Generate nodes and edges
    node_head, node_data = get_data('nodes.csv')
    edge_head, edge_data = get_data('edges.csv')

    #Instantiate graph object
    G = nx.Graph()

    #Populate graph object with filedata
    for node in node_data:
        id = node[0].replace('\'','')
        id = int(id)
        #print(node)
        G.add_node(id, name=node[1])
    for edge in edge_data:
        src = int(edge[0].replace('\'',''))
        dst = int(edge[1].replace('\'',''))
        #print(edge)
        G.add_edge(src,dst,fail_rate=edge[2],state=edge[3],score=edge[4])

    #run simulation infinitely until user exits
    flag = '0'
    while flag == '0':
        print("To run simulation type '0' without quotes.")
        flag = input("To exit type '1': ")

        fail_rate = nx.get_edge_attributes(G,"fail_rate")
        
        for edge1, edge2 in fail_rate:
            
            fail_check = randint(0,10)

            #if edge attribute's fail_rate is above this fail_check value, set the edge_attribute status to "DOWN", otherwise set to "UP"
            if int(fail_rate[(edge1,edge2)]) >= fail_check:
                G[edge1][edge2]['state'] = 'DOWN'
            
            #current state monitored
            current_state = nx.get_edge_attributes(G,'state')
            print(current_state[(edge1,edge2)])

            #only increments score if coming from a down state
            if int(fail_rate[(edge1,edge2)]) < fail_check and current_state[(edge1,edge2)] == 'DOWN':
                G[edge1][edge2]['state'] = 'UP'


        state = nx.get_edge_attributes(G,"state")
        for edge1, edge2 in state:
            print(edge1, edge2, state[(edge1,edge2)])



fault_routing()
#def __init__():