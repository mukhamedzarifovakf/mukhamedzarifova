import networkx as nx
import matplotlib.pyplot as plt


def dfs_tree(g, start, counted, tree_graph):
    counted.append(start)
    for neighbour in g[start]:
        if neighbour not in counted:
            dfs_tree(g, neighbour, counted, tree_graph)
            tree_graph.add_edge(start, neighbour, weight=0)
    return tree_graph


def bfs_tree(g, start, counted, tree_graph):
    counted.append(start)
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if neighbour not in counted:
                queue.append(neighbour)
                counted.append(neighbour)
                tree_graph.add_edge(current, neighbour, weight=0)
    return tree_graph


def dejkstra(G, start):
    shortest_paths = {vertex: float("inf") for vertex in G}
    shortest_paths[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in G(current):
            offering_path = shortest_paths(current) + G[current][neighbour]
            if offering_path < shortest_paths(neighbour):
                shortest_paths(neighbour) = offering_path
                queue.append(neighbour)
    return shortest_paths


def get_graph(file):
    G = nx.Graph()
    for line in file:
        line = line.strip()
        vertex1, vertex2, weight = line.split()
        G.add_edge(vertex1, vertex2, weight=float(weight))
    return G


file = open('input.txt', 'r')
map = get_graph(file)
counted = []
for point in map:
    if map not in counted:
        tree = nx.Graph()
        tree = bfs_tree(map, point, counted, tree)
        pos_tree = nx.spring_layout(tree)
        # nx.draw_networkx_labels(tree, pos_tree,font_size=15,font_family='sans-serif')
        nx.draw_networkx_nodes(tree, pos_tree, node_size=500)
        nx.draw_networkx_edges(tree, pos_tree,width=6)
print(counted)
plt.savefig("Graph")
plt.show()