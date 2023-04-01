class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u,v,w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        parent = []
        rank = []
        result = []
        i,e = 0,0 
        self.graph = sorted(self.graph, key = lambda item:item[2])

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        
        while e < self.vertices-1:
            u,v,w = self.graph[i]
            i+=1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e+1
                result.append([u,v,w])
                self.apply_union(parent, rank, x, y)
        
        for u,v,weight in result:
            print("%d - %d : %d" % (u,v, weight))


graph = Graph(6)
edge_list = [(0, 1, 4),(0, 2, 4),(1, 2, 2),(1, 0, 4),(2, 0, 4),(2, 1, 2),(2, 3, 3),(2, 5, 2),(2, 4, 4),(3, 2, 3),
             (3, 4, 3),(4, 2, 4),(4, 3, 3),(5, 2, 2),(5, 4, 3)]

for u,v,w in edge_list:
    graph.add_edge(u,v,w)

graph.kruskal_algo()

