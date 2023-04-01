nodes = ["A","B","C","D","E","F"]
edges = [("A","B"),("B","D"),("D","E"),("E","F"),("A","C"),("C","F"),]

class Graph:
    def __init__(self, nodes):
        self.graph = {}
        self.nodes = nodes
        for node in nodes:
            self.graph[node] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)


    def topological_sort_helper(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_helper(i,visited, stack)

        stack.append(v)

    def topologicalsort(self):
        visited = {node: False for node in self.nodes}
        stack = []

        for node in self.nodes:
            if visited[node] == False:
                self.topological_sort_helper(node, visited, stack)
        return stack[::-1]


graph = Graph(nodes)

for start, end in edges:
    graph.add_edge(start, end)

print(graph.topologicalsort())
