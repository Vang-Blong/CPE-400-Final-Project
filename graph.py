#Programmed by Blong Vang and Clint Vega
#CPE400 Final Project Spring 2022

#Graph class
class Graph:

    #build graph and number of nodes
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = []
    
    #connects nodes and adds edge properties
    #fail chance = random value 1-10 (each is 10%),of node to fail
    #score = defaults to 0, will dynamically attempt to calculate fail chance over time
    def add_edge(self, node1, node2, fail_chance, score=0):
        self.graph.append([node1,node2, fail_chance, score])

    
    def print_routing_table(self, distance):
        print("Node  Distance")
        for i in range(self.nodes):
            print("{0}\t\t{1}".format(i,distance[i]))

    def bellman_ford(self, origin):

        #generate initial routing table, setting all values to infinity and distance from self to 0
        distance = [float("infinity")] * self.nodes
        distance[origin] = 0

        #establishes reliability for all nodes in the graph using a score
        for _ in range(self.nodes - 1):
            for node1, node2, fail_chance, score in self.graph:
                if distance[node1] != float("infinity") and distance[node1] + score < distance[node2]:
                    distance[node2] = distance[1] + score
        
        self.print_routing_table(distance)