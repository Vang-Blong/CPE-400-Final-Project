import generate_files
import networkx as nx
import matplotlib.pyplot as plt
import cv2
import numpy

#import filedata
def get_data(filename):
    #opens .csv files, reads line by line
    with open(filename, "r", encoding="utf8") as input:
        lines = input.read().split("\n")
        data = [line.split(",") for line in lines]
        head = data[0]
        tail = data[1:]

    return head, tail[:-1]

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
        dst= int(edge[1].replace('\'',''))
        #print(edge)
        G.add_edge(src,dst,fail_rate=edge[2],state=edge[3],score=edge[4])

    #run simulation infinitely until user exits
    flag = '0'
    while flag == '0':
        print("To run simulation type '0' without quotes.")
        flag = input("To exit type '1': ")


fault_routing()
#def __init__():