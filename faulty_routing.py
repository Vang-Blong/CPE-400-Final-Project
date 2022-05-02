import networkx as nx
import matplotlib.pyplot as plt

#import filedata
def get_data(filename):
    #opens .csv files, reads line by line
    with open(filename, "r", encoding="utf8") as input:
        lines = input.read().split("\n")
        data = [line.split(",") for line in lines]
        head = data[0]
        tail = data[1:]

    return head, tail[:-1]

#def __init__():
#Generate nodes and edges
node_head, node_data = get_data('nodes.csv')
edge_head, edge_data = get_data('edges.csv')

#Instantiate graph object
G = nx.Graph()

#Populate graph object with filedata
for node in node_data:
    id = node[0].replace('\'','')
    id = int(id)
    G.add_node(id, name=node[1])
for edge in edge_data:
    src = int(edge[0].replace('\'',''))
    dst= int(edge[1].replace('\'',''))
    G.add_edge(src,dst,fail_rate=edge[2],score=edge[3])

#automatic metrics
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

#visualize using matplotlib
nx.draw_spring(G)
plt.show()