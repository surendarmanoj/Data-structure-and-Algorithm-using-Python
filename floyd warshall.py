edges = [["A","B",-1],["A","C",2],["B","C",3],["C","D",1],["B","E",1],["C","E",2],["D","E",2]]

nodes = ["A","B","C","D","E"]

class Graph:
    def __init__(self, edge, nodes):
        self.graph = []
        self.edges = edge
        self.nodes = nodes

        for i in range(len(self.nodes)):
            temp = []
            for j in range(len(self.nodes)):
                if i == j:
                    temp.append(0)
                else:
                    temp.append(float('inf'))
            self.graph.append(temp)
        
        for u, v,w in self.edges:
            self.graph[nodes.index(u)][nodes.index(v)] = w

    def floyd_warshall(self):
        for l in range(len(self.nodes)):
            for m in range(len(self.nodes)):
                for n in range(len(self.nodes)):
                    if m == n or l == m or l == n: 
                        pass
                    else:
                        if self.graph[m][l]+self.graph[l][n] < self.graph[m][n]:
                            self.graph[m][n] = self.graph[m][l] + self.graph[l][n]


    def print_Graph(self):
        for k in self.graph:
            print(k)
        print()

g = Graph(edges, nodes)
g.print_Graph()
g.floyd_warshall()
g.print_Graph()
