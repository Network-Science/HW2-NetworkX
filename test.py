import networkx as nx
import networkx.readwrite.edgelist as edgelist
from collections import deque
import networkx.algorithms.flow.utils as utils

mygraph = edgelist.read_edgelist("residual.edgelist", create_using=nx.DiGraph)
print(mygraph.nodes.data())
print(mygraph.edges.data())
print("\n")
residual = utils.build_residual_network(mygraph, 'capacity')
print(residual.nodes.data())
print(residual.edges.data())
