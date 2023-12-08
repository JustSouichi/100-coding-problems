def bfs(graph, start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited
