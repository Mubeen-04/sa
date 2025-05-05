def dfs_all_paths(graph, current, goal, visited, path, all_paths):
    visited.add(current)
    path.append(current)

    if current == goal:
        all_paths.append(list(path))
    else:
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                dfs_all_paths(graph, neighbor, goal, visited, path, all_paths)

    path.pop()
    visited.remove(current)

def dfs_shortest_path(graph, start, goal):
    visited = set()
    all_paths = []
    dfs_all_paths(graph, start, goal, visited, [], all_paths)

    print("All Paths (DFS):", all_paths)

    if all_paths:
        shortest = min(all_paths, key=len)
        print("Shortest Path (DFS):", shortest)
    else:
        print("No path found.")

# Example graph
graph = {
    '0': ['1', '2'],
    '1': ['0', '2'],
    '2': ['0', '1', '3', '4'],
    '3': ['2'],
    '4': ['2']
}

dfs_shortest_path(graph, '0', '2')
