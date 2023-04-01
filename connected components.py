edges = [["A","B"],["A","C"],["A","D"],["D","E"],["B","E"],
         ["F","H"],["F","G"],["I","J"]]
nodes = ["A","B","C","D","E","F","G","H","I","J","K"]


class Graph:
    def __init__(self, nodes, edges):
        self.graph = {}

        self.nodes = nodes
        for node in self.nodes:
            self.graph[node] = []

        self.edges = edges
        for u,v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)


    def dfs(self, node, visited):
        visited.add(node)
        count = 0
        for item in self.graph[node]:
            if item not in visited:
                count += self.dfs(item, visited)
        return count + 1
    
    def find_connected(self):
        visited = set()
        answer = []
        for item in self.nodes:
            if item not in visited:
                answer.append(self.dfs(item, visited))
        print(answer)


    def print_graph(self):
        print(self.graph)


g = Graph(nodes, edges)
g.print_graph()
g.find_connected()