import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
edges = []
boolean = True

print("Create a program that takes user’s input and then produce and visualize a directed network using NetworkX. User input is specified in the form of adjacency matrix.")

while(boolean):
    print("type your edge by inputting two integers at a time")
    first = int(input("type a first integer(node):"))
    second = int(input("type a second integer(node):"))
    edges.append((first, second))
    boolean = int(
        input("If you still have edges, press 1. Otherwise, press 0: "))


G.add_edges_from(edges)
plt.figure(figsize=(9, 9))
nx.draw_networkx(G, with_label=True, node_color='green')
plt.show()
