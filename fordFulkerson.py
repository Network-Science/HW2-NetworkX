import networkx.generators.random_graphs as generators
import time
import networkx as nx
import networkx.readwrite.edgelist as edgelist
import networkx.algorithms.shortest_paths.weighted as weighted
import networkx.algorithms.flow as flow
from collections import deque


def FordFulkersonBFS(G, s, t):
    # Start with flow f that is 0 on all edges
    flow = 0
    r = nx.algorithms.flow.utils.build_residual_network(G, 'capacity')
    # While there is a flow f` in G_f with v(f`) > 0 do
    path = Explore(r, s, t)
    while path != []:
        # Find bottle neck capacity of found path
        minn = minCapacity(r, path)
        # f = f + f`
        flow += minn
        # Update residual graph
        r = modifyResidual(r, path, minn)
        # Find new path from the residual graph
        path = Explore(r, s, t)
    return flow


def FordFulkersonDijkstra(G, source, sink):
    # Start with flow f that is 0 on all edges
    flow = 0
    # Create a residual graph
    residual = nx.algorithms.flow.utils.build_residual_network(G, 'capacity')
    while True:
        # dijkstra_path raises an error if there is no path, we used try except as a result
        # Try except = while there is a flow f` in G_f with v(f`) > 0 do
        try:
            # Find shortes path using dijkstra algorithm
            # pass in lamda function to avoid dijkstra to choosing edge with 0 capacity on path
            path = weighted.dijkstra_path(
                residual, source, sink, weight=lambda u, v, d: 1 if d['capacity'] != 0 else None)
            # find bottle neck capacity of shortest dijkstra path
            minn = minCapacity(residual, path)
            # f = f + f`
            flow += minn
            # update G_f
            residual = modifyResidual(residual, path, minn)
        except:
            break
    return flow

# minCapacity: Finds bottleneck Capacity of the path


def minCapacity(r, path):
    minFlow = None
    currentFlow = None
    for x in range(len(path) - 1):
        currentFlow = r[path[x]][path[x + 1]]['capacity']
        if minFlow == None or currentFlow < minFlow:
            minFlow = currentFlow
    return minFlow

# modifyResidual: Update residual graph after augmenting the flow


def modifyResidual(r, path, minFlow):
    for x in range(len(path) - 1):
        r[path[x]][path[x + 1]]['capacity'] -= minFlow
        # r[path[x + 1]][path[x]]['capacity'] += minFlow
    return r


def Explore(G, u, v):
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

    # Set Visited[u] = True
    Visited[list(G).index(u)] = True

    # Make tree T with root as u
    predec = {}
    predec[u] = '-1'

    # While ToExplore is non-empty
    while ToExplore:
        # Remove node x from ToExplore
        x = ToExplore.popleft()

        # for each edge (x,y) in Adj(x) do
        for y in G[x]:
            # if (Visited[y] == False)
            # G[x][y]['capacity] != 0 is used for residual graph
            if Visited[list(G).index(y)] == False and G[x][y]['capacity'] != 0:
                # Set Visited[y] = True
                Visited[list(G).index(y)] = True
                # Add y to ToExplore
                ToExplore.append(y)
                # Add y to S
                S.append(y)
                # Add y to T with x as its parents
                predec[y] = x

                # build path
                if y == v:
                    pathList = []
                    pathList.append(y)
                    while predec[y] != '-1':
                        pathList.append(predec[y])
                        y = predec[y]
                    pathList.reverse()
                    return pathList
    # Output S
    return []


print("\n Test case 1")
mygraph = edgelist.read_edgelist("MaxFlow1.edgelist", create_using=nx.DiGraph)
print('Ford Fulkerson with BFS', FordFulkersonBFS(mygraph, '0', '5'))
print("Ford Fulkerson with Dijkstra", FordFulkersonDijkstra(mygraph, '0', '5'))
print("max flow from library",
      flow.maximum_flow_value(mygraph, '0', '5'))

print("\n Test case 2")
mygraph = edgelist.read_edgelist("MaxFlow2.edgelist", create_using=nx.DiGraph)
print('Ford Fulkerson with BFS', FordFulkersonBFS(mygraph, '0', '5'))
print("Ford Fulkerson with Dijkstra", FordFulkersonDijkstra(mygraph, '0', '5'))
print("max flow from library",
      flow.maximum_flow_value(mygraph, '0', '5'))

print("\n Test case 3")
mygraph = edgelist.read_edgelist("MaxFlow3.edgelist", create_using=nx.DiGraph)
print('Ford Fulkerson with BFS', FordFulkersonBFS(mygraph, '1', '4'))
print("Ford Fulkerson with Dijkstra", FordFulkersonDijkstra(mygraph, '1', '4'))
print("max flow from library",
      flow.maximum_flow_value(mygraph, '1', '4'))


def testCase(node, edge):
    testGraph = generators.gnm_random_graph(node, edge, directed=True)
    startFF_BFS = time.time()
    BFS = FordFulkersonBFS(testGraph, 0, node-1)
    endFF_BFS = time.time()
    print("Time performance on Ford Fulkerson BFS", endFF_BFS-startFF_BFS)
    startFF_Dijkstra = time.time()
    Dijkstra = FordFulkersonDijkstra(testGraph, 0, node-1)
    endFF_Dijkstra = time.time()
    print("Time performance on Ford Fulkerson FFdijk",
          endFF_Dijkstra-startFF_Dijkstra)


print("\nTest case 1")
testCase(100, 300)

print("\nTest case 2")
testCase(1000, 5000)

print("\nTest case 3")
testCase(5000, 8000)
