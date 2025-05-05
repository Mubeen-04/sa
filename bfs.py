from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    traversal = []

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        traversal.append(node)

        if node == goal:
            print("BFS Traversal:", traversal)
            print("Start Node:", start)
            print("Goal Node:", goal)
            print("Path from Start to Goal:", path)
            return

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # Goal not reachable
    print("BFS Traversal:", traversal)
    print("Start Node:", start)
    print("Goal Node:", goal)
    print("Path from Start to Goal: None")

# Example graph
graph = {
    '0': ['1', '2'],
    '1': ['0', '2'],
    '2': ['0', '1', '3', '4'],
    '3': ['2'],
    '4': ['2']
}

bfs(graph, '0', '2')
