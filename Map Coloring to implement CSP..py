def is_valid(colored_map, node, color, graph):
    for neighbor in graph[node]:
        if neighbor in colored_map and colored_map[neighbor] == color:
            return False
    return True


def map_coloring(graph, colors, colored_map, node):
    if node is None:
        return True

    for color in colors:
        if is_valid(colored_map, node, color, graph):
            colored_map[node] = color
            if map_coloring(graph, colors, colored_map, select_unassigned_node(colored_map, graph)):
                return True
            colored_map[node] = None

    return False


def select_unassigned_node(colored_map, graph):
    for node in graph:
        if node not in colored_map or colored_map[node] is None:
            return node
    return None


def solve_map_coloring(graph, colors):
    colored_map = {node: None for node in graph}
    if map_coloring(graph, colors, colored_map, select_unassigned_node(colored_map, graph)):
        return colored_map
    else:
        return None


# Example usage:
if __name__ == "__main__":
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    colors = ['Red', 'Green', 'Blue']

    solution = solve_map_coloring(graph, colors)
    if solution:
        print("Solution found:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found")
