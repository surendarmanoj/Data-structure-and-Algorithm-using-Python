graph = {
    'A': [('B', 7), ('C', 8)],
    'B': [('A', 3), ('C', 3), ('D', 6), ('D', 8)],
    'C': [('A', 8), ('B', 3), ('D', 4), ('E', 3)],
    'D': [('B', 8), ('B', 6), ('C', 4), ('E', 2)],
    'E': [('D', 2), ('C', 3), ('F', 2)],
    'F': [('D', 5), ('E', 2),('F', 1)]
}


def prims_mst(graph):
    visited = set()
    mst = {}
    starting_node = list(graph.keys())[0]
    visited.add(starting_node)

    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None
        for node in visited:
            for neighbour, weight in graph[node]:
                if neighbour not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (node, neighbour, weight)

        if min_edge:
            mst.setdefault(min_edge[0],[]).append((min_edge[1],min_edge[2]))
            mst.setdefault(min_edge[1],[]).append((min_edge[0],min_edge[2]))
            visited.add(min_edge[1])

    return mst

print(prims_mst(graph))