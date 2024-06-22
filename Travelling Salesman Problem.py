import itertools


def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance_matrix[route[i - 1]][route[i]]
    return total_distance


def travelling_salesman_problem(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    shortest_route = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities):
        current_distance = calculate_total_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = perm

    return shortest_route, min_distance


# Example usage:
if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, distance = travelling_salesman_problem(distance_matrix)
    print("Shortest route:", route)
    print("Minimum distance:", distance)
