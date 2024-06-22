def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)
    print(start, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': ['H'],
        'F': [],
        'G': [],
        'H': []
    }

    start_node = 'A'
    print("Depth-First Search starting from node " + start_node + ":")
    dfs(graph, start_node)
