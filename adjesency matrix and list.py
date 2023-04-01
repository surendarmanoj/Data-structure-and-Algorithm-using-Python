nodes = ["A","B","C","D","E"]
edges =[("A","B"),("A","C"),("D","B"),("C","D"),("C","E"),("D","E") ]

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self,start, end):
        self.adj_list[start].append(end)
        self.adj_list[end].append(start)
        
    def print_adj_list(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])


graph = Graph(nodes)

for u,v in edges:
    graph.add_edge(u,v)

graph.print_adj_list()