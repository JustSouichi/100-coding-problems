def kruskal(graph):
    parent = [i for i in range(len(graph))]
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    def union(i, j):
        a = find(i)
        b = find(j)
        parent[a] = b

    edges = sorted([(graph[i][j], i, j) for i in range(len(graph)) for j in range(len(graph[i])) if graph[i][j] != 0])
    min_span_tree = []
    total_cost = 0

    for edge in edges:
        weight, u, v = edge
        if find(u) != find(v):
            union(u, v)
            min_span_tree.append(edge)
            total_cost += weight

    return min_span_tree, total_cost
