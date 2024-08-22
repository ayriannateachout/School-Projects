import networkx as nx
import matplotlib.pyplot as plt


#read data from file and construct graph
def construct_graph(file_path):
    g = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            src, dest, weight = line.strip().split(', ')
            g.add_edge(src, dest, weight=float(weight))
    return g


# visualize the graph
def visualize_graph(g):
    nx.draw(g, with_labels=True)
    plt.show()


#perform bfs traversal
def bfs_traversal(g, start):
    traversal_order = list(nx.bfs_edges(g, start))
    print("bfs traversal order:", traversal_order)


#perform dfs traversal
def dfs_traversal(g, start):
    traversal_order = list(nx.dfs_edges(g, start))
    print("dfs traversal order:", traversal_order)


#calculate shortest paths using dijkstra's algorithm
def dijkstra_shortest_paths(g, source):
    shortest_paths = nx.single_source_dijkstra(g, source)
    print("shortest paths (dijkstra's algorithm):", shortest_paths)


#calculate shortest paths using bellman-ford algorithm
def bellman_ford_shortest_paths(g, source):
    shortest_paths = nx.single_source_bellman_ford(g, source)
    print("shortest paths (bellman-ford algorithm):", shortest_paths)


# find minimum spanning tree
def find_minimum_spanning_tree(g):
    min_spanning_tree = nx.minimum_spanning_tree(g)
    print("minimum spanning tree:", min_spanning_tree.edges())


#main function
if __name__ == "__main__":
    file_path = "city_distances.txt"
    graph = construct_graph(file_path)

    visualize_graph(graph)

    start_city = 'Lamoni'
    bfs_traversal(graph, start_city)
    dfs_traversal(graph, start_city)

    dijkstra_shortest_paths(graph, start_city)
    bellman_ford_shortest_paths(graph, start_city)

    find_minimum_spanning_tree(graph)
