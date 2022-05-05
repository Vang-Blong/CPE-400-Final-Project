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
    print("Input number of simulations to run desired. ")
    print("To simulate rerouting paths with randomized failures on a single instance, input '1'")
    print("To return an accurate display of overall network connectivity, an integer >10000 is recommended.")
    flag = input("Otherwise, type '0' to exit: ")
    #if flag is 0, exit
    if flag == 0:
        return 0

    counter = 1
    G_temp = G.copy()

    while int(flag) > 0:

        #iterate on failure_rate the flag# of times
        fail_rate = nx.get_edge_attributes(G,"fail_rate")

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
            
            #get score by dividing number of successes by instances ran
            current_up = nx.get_edge_attributes(G,'up_count')
            current_score = 100 - int(current_up[(edge1,edge2)]) / counter * 100
            
            #print(100 - current_score * 100)
            G[edge1][edge2]['score'] = current_score

            #current state monitored
            current_state = nx.get_edge_attributes(G,'state')
            #if something goes down, remove the edge from the Graph copy
            if current_state[(edge1,edge2)] == 'DOWN':
                if G_temp.has_edge(edge1,edge2):
                    G_temp.remove_edge(edge1,edge2)
                

        flag = int(flag) - 1
        counter += 1

    
    #Put scores in list for printing to screen and Graph analysis
    originalScoreList = []
    for edge1, edge2, data in G.edges(data=True):
        originalScoreList.append(int(data['fail_rate']))
    finalScoreList = []
    for edge1, edge2, data in G.edges(data=True):
        finalScoreList.append(int(data['score']))

    #determines shortest paths table using dijkstras algorithm & length using the Graph copy
    paths = dict(nx.all_pairs_dijkstra_path(G_temp))
    lengths = dict(nx.all_pairs_dijkstra_path_length(G_temp))

    #prints routing table with shortest routes and length
    print("Routing Table")
    print("Source : { Dst: [Route], ... }")
    count = 0
    for key in paths:
        print(str(count) + " : " + str(paths[key]))
        count += 1
    count = 0
    print("Source : { Dst: Length, ... }")
    for key in lengths:
        print(str(count) + " : " + str(lengths[key]))
        count += 1
        
    count = 0
    print("Path : Actual Fail Rate : Reverse Calculated Fail Score")
    for edge in G.edges():
        print(str(edge) + " : "  + str(originalScoreList[count]) + " : "  + str(finalScoreList[count]))
        count += 1

    #Visualizing graph based on score
    edges,score = zip(*nx.get_edge_attributes(G,'score').items())
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color= score, edgelist=edges, edge_color=score, width=4.0, edge_cmap=plt.cm.jet)
    nx.draw_networkx_labels(G, pos, font_color='white', font_weight = 'bold')


    #Colorbar 
    legend = plt.cm.ScalarMappable(cmap=plt.cm.jet)
    legend.set_array(finalScoreList)
    plt.colorbar(legend, shrink = 0.5, label = 'Fail Rate Score')
    plt.show()

    

fault_routing()
#def __main__():