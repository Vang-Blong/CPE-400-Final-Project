import networkx as nx

def get_data(filename):

    with open(filename, "r", encoding="utf8") as input:
        lines = input.read.split("\n")
        data = [line.split(",") for line in lines]
        head = data[0]
        tail = [data[1:]

    return head, tail

node_header, node_data = get_data('nodes.csv')
edge_header, edge_data = get_data('edges.csv')
