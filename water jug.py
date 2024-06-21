from collections import deque


def is_solvable(x, y, z):
    # To check if the problem is solvable
    if x + y < z:
        return False
    if x == 0 or y == 0:
        return z == 0 or x + y == z
    return z % gcd(x, y) == 0


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def bfs(x, y, z):
    # Initialize the queue with the initial state (0, 0)
    queue = deque([(0, 0)])
    visited = set((0, 0))

    while queue:
        a, b = queue.popleft()

        if a == z or b == z or a + b == z:
            return True

        # List all possible next states
        next_states = [
            (x, b),  # Fill Jug 1
            (a, y),  # Fill Jug 2
            (0, b),  # Empty Jug 1
            (a, 0),  # Empty Jug 2
            (min(a + b, x), a + b - min(a + b, x)),  # Pour Jug 2 into Jug 1
            (a + b - min(a + b, y), min(a + b, y))  # Pour Jug 1 into Jug 2
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    return False


def water_jug_problem(x, y, z):
    if is_solvable(x, y, z):
        return bfs(x, y, z)
    else:
        return False


# Example usage:
x = 3
y = 5
z = 4

if water_jug_problem(x, y, z):
    print(f"It is possible to measure {z} liters using the jugs of capacities {x} and {y}.")
else:
    print(f"It is not possible to measure {z} liters using the jugs of capacities {x} and {y}.")
