#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022
#Generates random .csv file used for importing graph data

from random import random,randint  #for random graph on every instance

def generate_files():
    #dictionary for mapping number to alphabet character
    num_map = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

     # designates and generates graph with random # of nodes
    num_nodes = randint(5,25)

    #need 2 trackers to ensure every node has an edge
    tracker= []
    tracker2 = []

    for node in range(0, num_nodes):
        tracker.append(node)
        tracker2.append(node)

    #create/restart new .csv file for graph data
    initial1 = open("nodes.csv",'w')
    initial2 = open("edges.csv",'w')

    initial1.write("id,name\n")
    initial2.write("src,dst,fail_rate,score\n")
    initial1.close()
    initial2.close()

    #append data to graph files
    input1 = open("nodes.csv",'a')
    for num in range(num_nodes):
            input1.write(str(num) + "," + num_map[num] + '\n')


    input2 = open("edges.csv",'a')
    #exits when every node gets an edge and connects graph
    while len(tracker) > 0 and len(tracker2) > 0:
        #picks two different edges
        edge1 = randint(0,num_nodes - 2)
        edge2 = randint(edge1 + 1, num_nodes - 1)
        #generates unique chance to fail
        fail_chance = randint(0,10)
        
        #ensures every node gets an edge and is connected to whole graph
        if edge1 in tracker:
            tracker.remove(edge1)
        if edge2 in tracker:
            tracker.remove(edge2)
        
        if edge1 not in tracker:
            if edge1 in tracker2:
                tracker2.remove(edge1)
        if edge2 not in tracker:
            if edge2 in tracker2:
                tracker2.remove(edge2)    

        #populates graph with randomized edge values
        input2.write(str(edge1) + "," + str(edge2) + "," + str(fail_chance) + "," + str(1) + '\n')

generate_files()
#def __init__():
#    generate_files()
        
        
