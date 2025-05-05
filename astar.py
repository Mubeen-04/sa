from queue import PriorityQueue

def a_star_search(graph, heuristics, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    
    g_costs = {start: 0}
    parent = {start: None}
    f_costs = {start: heuristics[start]}

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], f_costs[goal]

        for neighbor, cost in graph[current]:
            tentative_g_cost = g_costs[current] + cost

            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristics[neighbor]
                f_costs[neighbor] = f_cost
                open_list.put((f_cost, neighbor))
                parent[neighbor] = current

    return None, float('inf')


# Graph and heuristic definition
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 3)],
    'C': [('E', 5)],
    'D': [('F', 2), ('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

heuristics = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}

# Run A* search
start_node = 'A'
goal_node = 'G'
path, total_cost = a_star_search(graph, heuristics, start_node, goal_node)

print("Path:", path)
print("Total Cost (f(n)):", total_cost)
