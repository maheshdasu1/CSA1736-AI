import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost from current node to goal
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, heuristics, start, goal):
    # Open list (priority queue)
    open_list = []
    heapq.heappush(open_list, Node(start, None, 0, heuristics[start]))

    # Closed list (visited nodes)
    closed_list = set()

    while open_list:
        # Get the node with the lowest cost
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.name)

        # Check if the goal has been reached
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Explore neighbors
        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue

            g = current_node.g + cost
            h = heuristics[neighbor]
            neighbor_node = Node(neighbor, current_node, g, h)

            if neighbor_node not in open_list:
                heapq.heappush(open_list, neighbor_node)
            else:
                for node in open_list:
                    if node.name == neighbor and node.f > neighbor_node.f:
                        node.g = g
                        node.h = h
                        node.f = neighbor_node.f
                        node.parent = current_node
                        break

    return None  # No path found

# Example usage:
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'D': 1, 'E': 5},
        'C': {'A': 3, 'F': 2},
        'D': {'B': 1},
        'E': {'B': 5, 'H': 1},
        'F': {'C': 2, 'G': 1},
        'G': {'F': 1},
        'H': {'E': 1}
    }

    # Heuristic values for each node
    heuristics = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 6,
        'E': 1,
        'F': 1,
        'G': 0,
        'H': 0
    }

    start_node = 'A'
    goal_node = 'G'
    path = a_star(graph, heuristics, start_node, goal_node)
    if path:
        print("Path found:", path)
    else:
        print("No path found")
