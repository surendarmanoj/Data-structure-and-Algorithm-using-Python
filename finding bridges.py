edges = [["A","B"],["B","E"],["B","C"],["C","D"],["D","E"],["D","F"],["B","F"],["C","G"],["F","G"],["C","H"],["H","I"],["H","J"],["I","J"],["I","K"],["J","L"],["K","L"],["K","M"],["M","N"],["M","O"],["N","O"]]
nodes = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]


class Graph:
    def __init__(self, edges, nodes):
        self.graph = {}
        self.visited = {}
        self.intime = {}
        self.lowtime = {}
        self.nodes = nodes
        self.edges = edges
        self.timer = 1
        for i in self.nodes:
            self.graph[i] = []
            self.visited[i] = False
            self.intime[i] = None
            self.lowtime[i] = None
        for u,v in self.edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def dfs(self, node, parent):
        self.visited[node] = True
        self.intime[node] = self.timer
        self.lowtime[node] = self.timer
        self.timer += 1

        for child in self.graph[node]:
            if not self.visited[child]:
                self.dfs(child,node)
                if self.intime[node] < self.lowtime[child]:
                    print("Bridge found between ",node," - ", child)
                self.lowtime[node] = min(self.lowtime[node], self.lowtime[child])
            else:
                if child != parent:
                    self.lowtime[node] = min(self.lowtime[node], self.intime[child])

    def findBirdge(self):
        self.dfs("A",-1)


    def print_graph(self):
        print(self.graph)
        print(self.intime)
        print(self.lowtime)
        print(self.visited)



g = Graph(edges, nodes)
g.findBirdge()
g.print_graph()