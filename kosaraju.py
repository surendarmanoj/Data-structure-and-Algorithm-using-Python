graph = {'a': ['b'],
         'b': ['c','d'],
         'c': ['a','e'],
         'd': ['e','g'],
         'e': ['f'],
         'f': ['d'],
         'g': ['h'],
         'h': ['f','i'],
         'i': ['j'],
         'j': []}


def kosaraju(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(node)

    for node in graph.keys():
        if node not in visited:
            dfs(node)

    graph_rev = {}
    for node in graph.keys():
        graph_rev[node] = []
    for node in graph.keys():
        for neighbour in graph[node]:
            graph_rev[neighbour].append(node)

    visited.clear()
    sccs = []

    def scc(node, component):
        visited.add(node)
        component.append(node)
        for neighbour in graph_rev[node]:
            if neighbour not in visited:
                scc(neighbour, component)

    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            scc(node, component)
            sccs.append(component)
    return sccs

sccs_list = kosaraju(graph)
print(sccs_list)
