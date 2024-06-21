from collections import deque


def bfs(graph, start):
    # Create a queue for BFS and enqueue the start node
    queue = deque([start])

    # Set of visited nodes to avoid revisiting
    visited = set([start])

    # While the queue is not empty
    while queue:
        # Dequeue a vertex from the queue
        node = queue.popleft()

        # Print or process the node
        print(node, end=' ')

        # Enqueue all adjacent nodes that have not been visited
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


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
    print("Breadth-First Search starting from node " + start_node + ":")
    bfs(graph, start_node)
