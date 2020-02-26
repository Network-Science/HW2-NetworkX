import networkx as nx
import networkx.readwrite.edgelist as edgelist
from collections import deque
import networkx.algorithms.flow.utils as utils


def Explore(G, u):
    # n = |V| for G = (V, E)
    n = len(G.nodes())
    # Initialize Visited array as false
    Visited = [False for i in range(n)]
    # Create queue object using deque for ToExplore
    ToExplore = deque()
    # Create List S
    S = []
    # Add u to ToExplore and to S
    ToExplore.append(u)
    S.append(u)
    # Visited[u] = True
    Visited[list(G).index(u)] = True
    # While ToExplore is non-empty
    while ToExplore:
        # Remove node x from ToExplore
        x = ToExplore.popleft()
        # for each edge (x,y) in Adj(x) do
        for y in G[x]:
            # if (Visited[y] == False)
            if Visited[list(G).index(y)] == False:
                # Set Visited[y] = True
                Visited[list(G).index(y)] = True
                # Add y to ToExplore
                ToExplore.append(y)
                # Add y to S
                S.append(y)
    # Output S
    return(S)


mygraph = edgelist.read_edgelist("test2.edgelist", create_using=nx.DiGraph)
result = Explore(mygraph, '1')
print(result)


def FordFulkerson(G, source, sink):
    parent = [-1]*(len(G.nodes()))
    max_flox = 0
    while sink in Explore(G, source):
        path_flow = float("Inf")
        s = sink
        while(s != source):
