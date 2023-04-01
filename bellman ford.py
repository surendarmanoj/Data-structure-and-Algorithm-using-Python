edges = [["A","B",6],["A","C",4],["A","D",5],["C","B",-2],["D","C",-2],["B","E",-1],["C","E",2],["D","F",-1],["E","F",3]]
vertices = ["A","B","C","D","E","F"]

class Graph:
    def __init__(self, vertices, edges):
        self.distance = {}
        self.vertices = vertices
        for i in self.vertices:
            self.distance[i] = float('inf')
        self.edges = edges
        self.track_change = []

    def Bellman_ford(self):
        for _ in range(len(self.vertices)-1):
            self.distance["A"] = 0
            t1 = []
            for l,m in self.distance.items():
                t1.append((l,m))
            changed = False

            for u, v,w in self.edges:
                if self.distance[u] < float('inf') and w + self.distance[u] < self.distance[v]:
                    self.distance[v] = w + self.distance[u]
                    changed =True
            self.track_change.append(t1)
            if changed == False:
                break
        
        for k in self.track_change:
            print(k)
        

g = Graph(vertices, edges)
g.Bellman_ford()