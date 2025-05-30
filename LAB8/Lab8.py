import heapq
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Urziceni': 85, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}
heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}
def greedy_bfs(start, goal):
    pq = [(heuristics[start], start, [start])]
    visited = set()
    
    while pq:
        _, current, path = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        
        if current == goal:
            return path
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))
    return []

def a_star_search(start, goal):
    pq = [(heuristics[start], 0, start, [start])]
    visited = set()
    while pq:
        _, cost, current, path = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        
        if current == goal:
            return path
        
        for neighbor, distance in graph[current].items():
            if neighbor not in visited:
                new_cost = cost + distance # g(n) = actual cost so far
                f_value = new_cost + heuristics[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(pq, (f_value, new_cost, neighbor, path + [neighbor]))
    return []
start_city = 'Arad'
goal_city = 'Bucharest'

gbfs_path = greedy_bfs(start_city, goal_city)
a_star_path = a_star_search(start_city, goal_city)

print("Greedy BFS Path:", gbfs_path)
print("A* Path:", a_star_path)
