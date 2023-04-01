# Example graph with a cycle
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['D']
}

def is_cycle_present(graph):
    visited = set()
    stack = set()

    def dfs(node):
        visited.add(node)
        stack.add(node)

        for neighbour in graph.get(node):
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
                
            elif neighbour in stack:
                return True
        
        stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

print(is_cycle_present(graph))