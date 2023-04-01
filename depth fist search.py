adj_list = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B","F"],
    "D":[],
    "E":["F"],
    "F":[]
}

color = {} # completely visited -> white, visited -> Green, not visited-> black
parent = {}
trav_time = {} #[start, end]
dfs_op = []

for node in adj_list.keys():
    color[node] = "B"
    parent[node] = None
    trav_time[node] = [-1,-1]
time = 0
def dfs(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_op.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == "B":
            parent[v] = u
            dfs(v)
    color[u] = "W"
    trav_time[u][1] = time
    time += 1

dfs("A")   
print(color)
print(parent)
print(trav_time)
print()

for node in adj_list.keys():
    print(node, "->", trav_time[node])