graph_dir = {
    "A":{"B":10, "C":5},
    "B":{"D":1},
    "C":{"B":3, "D":9, "E":2},
    "D":{},
    "E":{"A":2, "D":6}
    
}


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.shortest_distance = {}
        self.parent = {}
        self.visited = graph
        self.trackpath = []

    def dijiktras(self, start, end):
        for node in self.visited:
            self.shortest_distance[node] =float('inf')
        self.shortest_distance[start] = 0

        while self.visited:
            min_distance_node = None
            for node in self.visited:
                if min_distance_node == None:
                    min_distance_node = node
                elif self.shortest_distance[node] < self.shortest_distance[min_distance_node]:
                    min_distance_node = node
                
                for child, weight in self.graph[min_distance_node].items():
                    if weight + self.shortest_distance[min_distance_node] < self.shortest_distance[child]:
                        self.shortest_distance[child] = weight + self.shortest_distance[min_distance_node]
                        self.parent[child] = min_distance_node
            self.visited.pop(min_distance_node)

        curNode = end
        while curNode != start:
            try:
                self.trackpath.insert(0, curNode)
                curNode = self.parent[curNode]
            except:
                print("Path not reachable")
                break
        self.trackpath.insert(0, start)

        if self.shortest_distance[end] != float('inf'):
            print("Shortest Distance is " + str(self.shortest_distance[end]))
            print("optimal Path is" + str(self.trackpath))


g = Graph(graph_dir)
g.dijiktras("A","D")