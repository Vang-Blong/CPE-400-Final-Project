import networkx as nx

#import filedata
def get_data(filename):

    #opens .csv, reads line by line
    with open(filename, "r", encoding="utf8") as input:
        lines = input.read.split("\n")
        data = [line.split(",") for line in lines]
        head = data[0]
        tail = [data[1:]

    return head, tail

#Generate nodes and edges
node_head, node_data = get_data('nodes.csv')
edge_head, edge_data = get_data('edges.csv')

#Instantiate raph object
G = nx.graph()

for node in node_data:
    G.add_node(int(node[0]), name=node[1], cname=node[2], year=node[3])