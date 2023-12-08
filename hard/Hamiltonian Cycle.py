def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n

    def is_safe(v, pos, path):
        if graph[path[pos - 1]][v] == 0:
            return False
        for vertex in path:
            if vertex == v:
                return False
        return True

    def ham_cycle_util(path, pos):
        if pos == n:
            if graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, n):
            if is_safe(v, pos, path):
                path[pos] = v
                if ham_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1

        return False

    path[0] = 0
    if not ham_cycle_util(path, 1):
        return None
    return path
