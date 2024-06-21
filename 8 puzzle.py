import heapq

# Define the initial and goal boards
initial_board = [
    [1, 3, 8],
    [4, 5, 6],
    [7, 0, 2]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Define the PuzzleState class
class PuzzleState:
    def __init__(self, board, empty_pos, moves=0, previous=None):
        self.board = board
        self.empty_pos = empty_pos
        self.moves = moves
        self.previous = previous
        self.priority = self.moves + self.manhattan_distance()

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

# Initialize the initial and goal states
initial_state = PuzzleState(initial_board, (2, 1))
goal_state = PuzzleState(goal_board, (2, 2))

# A* search implementation
open_set = []
heapq.heappush(open_set, initial_state)
closed_set = set()
solution = None

while open_set:
    current_state = heapq.heappop(open_set)

    if current_state.board == goal_state.board:
        solution = current_state
        break

    closed_set.add(current_state)

    x, y = current_state.empty_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [row[:] for row in current_state.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbor = PuzzleState(new_board, (nx, ny), current_state.moves + 1, current_state)

            if neighbor not in closed_set:
                heapq.heappush(open_set, neighbor)

# Print the solution
path = []
while solution:
    path.append(solution.board)
    solution = solution.previous
path.reverse()

for step in path:
    for row in step:
        print(' '.join(map(str, row)))
    print()
