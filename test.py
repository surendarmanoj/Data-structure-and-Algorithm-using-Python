# create a directed graph with 10 vertices
graph = {1: [(2, 1)],
         2: [(3, 2), (4, 3)],
         3: [(1, 4), (5, 5)],
         4: [(5, 6), (7, 7)],
         5: [(6, 8)],
         6: [(4, 9)],
         7: [(8, 10)],
         8: [(6, 11), (9, 12)],
         9: [(10, 13)],
         10: []}

# implement Kosaraju's algorithm
def kosaraju(graph):
    visited = set()
    stack = []

    # helper function to perform DFS on the graph
    def dfs(node):
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    # perform DFS on all unvisited nodes
    for node in graph.keys():
        if node not in visited:
            dfs(node)

    # create a reversed graph
    graph_rev = {}
    for node in graph.keys():
        graph_rev[node] = []
    for node in graph.keys():
        for neighbor, weight in graph[node]:
            graph_rev[neighbor].append((node, weight))

    visited.clear()
    sccs = []

    # helper function to find strongly connected components
    def scc(node, component):
        visited.add(node)
        component.append(node)
        for neighbor, weight in graph_rev[node]:
            if neighbor not in visited:
                scc(neighbor, component)

    # traverse the stack in reverse order and find SCCs
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            scc(node, component)
            sccs.append(component)

    return sccs

# run the algorithm and print the SCCs
sccs = kosaraju(graph)
print(sccs)

'''

   a --(1)--> b --(2)--> c
   ^           |         |
   |           v         v
  (4)          d --(6)--> e --(8)--> f
   |                      ^
   v                      |
   g --(10)--> h --(11)--> i --(13)--> j


'''