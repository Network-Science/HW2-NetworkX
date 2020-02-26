import networkx as nx
import matplotlib.pyplot as plt
import networkx.readwrite.edgelist as edgelist

# edgelist.write_edgelist(nx.path_graph(4), "test.edgelist")
mygraph = edgelist.read_edgelist("test.edgelist", create_using=nx.DiGraph)

plt.figure(figsize=(6, 6))
nx.draw_networkx(mygraph, with_label=True)
plt.show()
#print(len(mygraph.nodes()))
#print(mygraph.edges())

#print(mygraph.nodes.data())
#print(mygraph.edges.data())
