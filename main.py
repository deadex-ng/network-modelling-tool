"""The main entry point."""
import pandas as pd
from graph.graph import Graph
from utils.utils import unique, model_traffic

g = Graph()

df = pd.read_csv("network.csv")
(rows, cols) = df.shape

nodes_list = []
CAPACITY = 10
for i in range(rows):
    start = df.iat[i, 1]
    end = df.iat[i, 2]
    nodes_list.append(start)
    nodes_list.append(end)

unique_nodes_list = unique(nodes_list)

for node in unique_nodes_list:
    g.add_vertex(node)

for i in range(rows):
    start_node = df.iat[i, 1]
    end_node = df.iat[i, 2]
    weight = df.iat[i, 4]
    g.add_edge(start_node, end_node, weight)

# Remove link between A and B
# g.add_edge('A','B',0)

adj_matrix_graph = g.get_graph()


traffic_df = pd.read_csv("traffic.csv")
(row, col) = traffic_df.shape
traffic = {}
for i in range(row):
    source = traffic_df.iat[i, 0]
    destination = traffic_df.iat[i, 1]
    demand = traffic_df.iat[i, 2]
    traffic[source] = [destination, demand]

traffic_paths = []

for k, v in traffic.items():
    starting_point = k
    finishing_point = v[0]
    traffic_demand = v[1]
    starting_point_index = unique_nodes_list.index(starting_point)
    finishing_point_index = unique_nodes_list.index(finishing_point)
    traffic_path = model_traffic(
        adj_matrix_graph, starting_point_index, finishing_point_index, traffic_demand
    )
    traffic_paths.append(traffic_path)

for path in traffic_paths:
    nodes_path = [unique_nodes_list[i] for i in path[0]]
    print("Network Details For Traffic Path: ", nodes_path)
    traffic_node_pairs = []
    for i in range(len(path[0]) - 1):
        # print(path[0])
        traffic_node_pairs.append((path[0][i], path[0][i + 1]))
    for pair in traffic_node_pairs:
        print("source: ", unique_nodes_list[pair[0]])
        print("destination: ", unique_nodes_list[pair[1]])
        print("Capaicity: ", CAPACITY)
        print("Capacity Utilization: ", round((path[1] / CAPACITY) * 100), "%")
        print()
    print("===================================================")
