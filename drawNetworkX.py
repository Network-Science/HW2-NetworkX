import networkx as nx
import matplotlib.pyplot as plt
import networkx.readwrite.edgelist as edgelist

# Takes in user input
mygraph = edgelist.read_edgelist(
    "drawNetworkX.edgelist", create_using=nx.DiGraph)

plt.figure(figsize=(6, 6))
edges = mygraph.edges()
colors = [mygraph[u][v]['color'] for u, v in edges]
weights = [mygraph[u][v]['weight']/2 for u, v in edges]
# draw according to corresponding colors and weight of edges
nx.draw_networkx(mygraph, edges=edges, edge_color=colors,
                 width=weights, with_label=False)
plt.show()

print(mygraph.nodes.data())
print(mygraph.edges.data())
