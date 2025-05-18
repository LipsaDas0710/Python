import heapq
import numpy as np
def manhattan_distance(state, goal_state):
    distance = 0
    for num in range(1, 9):
        x1, y1 = np.where(state == num)
        x2, y2 = np.where(goal_state == num)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance[0]

def get_neighbors(state):
    neighbors = []
    x, y = np.where(state == 0)
    x, y = x[0], y[0]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = state.copy()
            new_state[x, y], new_state[nx, ny] = new_state[nx, ny], new_state[x, y]
            neighbors.append(new_state)
    
    return neighbors

def a_star_search(start_state, goal_state):
    priority_queue = [(manhattan_distance(start_state, goal_state), 0, start_state.tolist(), [])]
    visited = set()
    while priority_queue:
        _, cost, state_list, path = heapq.heappop(priority_queue)
        state = np.array(state_list)
        state_tuple = tuple(map(tuple, state))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        if np.array_equal(state, goal_state):
            return path + [state]
        for neighbor in get_neighbors(state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                heapq.heappush(priority_queue, (cost + 1 + manhattan_distance(neighbor, goal_state), 
                                                cost + 1, neighbor.tolist(), path + [state]))
    return []

# Define start and goal states
start_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
goal_state = np.array([[1, 2, 3], [8, 4, 0], [7, 6, 5]])

solution = a_star_search(start_state, goal_state)
if solution:
    print("Solution path:")
    for step in solution:
        print(np.array(step), "\n")
else:
    print("No solution found.")
