#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022
#Imports graph data and visualizes it using matplotlib

#import generate_files #for simulating a new graph in each instance
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
        G.add_node(id, name=node[1],fail_rate=node[2], state=node[3],up_count=node[4],down_count=node[5],score=node[6])
    for edge in edge_data:
        src = int(edge[0].replace('\'',''))
        dst = int(edge[1].replace('\'',''))
        #print(edge)
        G.add_edge(src,dst,fail_rate=edge[2],state=edge[3],up_count=edge[4],down_count=edge[5],score=edge[6])

    #run simulation number of times designated by flag & counts iterations for calculating score
    flag = 5000
    counter = 1
    while flag > 0:
        #print("To run simulation type '0' without quotes.")
        #flag = input("To exit type '1': ")

        #iterate on failure_rate the flag# of times
        fail_rate = nx.get_edge_attributes(G,"fail_rate")
        current_paths = dict(nx.all_pairs_dijkstra(G))

        #Create a copy of the original graph for mutating later
        G_temp = G.copy()
        for edge1, edge2 in fail_rate:
            fail_check = randint(0,100)
            
            #if edge attribute's fail_rate is above this fail_check value, set the edge_attribute status to "DOWN", otherwise set to "UP", then decrements the score value by 1
            if int(fail_rate[(edge1,edge2)]) >= fail_check:
                G[edge1][edge2]['state'] = 'DOWN'
                down_count = G[edge1][edge2]['down_count']
                down_count = int(down_count) + 1
                G[edge1][edge2]['down_count'] = down_count

            #increments score and sets state to up
            if int(fail_rate[(edge1,edge2)]) < fail_check:
                G[edge1][edge2]['state'] = 'UP'
                up_count = G[edge1][edge2]['up_count']
                up_count = int(up_count) + 1
                G[edge1][edge2]['up_count'] = up_count
            
            current_up = nx.get_edge_attributes(G,'up_count')
            current_score = int(current_up[(edge1,edge2)]) / counter
            #print(100 - current_score * 100)
            G[edge1][edge2]['score'] = current_score

            #current state monitored
            current_state = nx.get_edge_attributes(G,'state')
            #if something goes down, recalculate dijkstras
            if current_state[(edge1,edge2)] == 'DOWN':
                G_temp.remove_edge(edge1,edge2)
                current_paths = dict(nx.all_pairs_dijkstra(G_temp))
                for n, (dist,path) in nx.all_pairs_dijkstra(G_temp):
                    print(path)

        flag -= 1
        counter += 1


fault_routing()
#def __init__():