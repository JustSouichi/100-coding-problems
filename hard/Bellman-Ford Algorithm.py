def bellman_ford(graph, source):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight

    # Check for negative weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distance[vertex] + weight < distance[neighbor]:
                return "Graph contains a negative weight cycle"
    
    return distance
