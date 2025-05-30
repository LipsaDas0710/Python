def dfs_stack(graph, start_node, max_depth):
    stack = [(start_node, 0, [start_node])]  # (node, depth, path)
    visited = set()
    goal = "Bucharest"

    while stack:
        current_node, current_depth, path = stack.pop()

        if current_node not in visited:
            print(current_node)  
            visited.add(current_node)

            if current_node == goal:
                return path  # Return path when goal is found

            if current_depth < max_depth:
                for neighbor, _ in graph[current_node]:  
                    if neighbor not in visited:
                        stack.append((neighbor, current_depth + 1, path + [neighbor]))

    return []  # Return empty list if goal not found within depth limit

# Romania map with distances
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Iteratively increase depth limit until Bucharest is found
for depth in range(5):  
    print(f"\nTrying depth limit {depth}...")
    path = dfs_stack(romania_map, 'Arad', depth)
    
    if path:  # Stop if goal is found
        print(f"\nPath to Bucharest: {path}")
        break
