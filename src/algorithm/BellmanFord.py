def bellman_ford(graph, start):
    # 거리 정보를 무한대로 초기화
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0

    # 정점 수만큼 반복하여 최단 거리를 업데이트
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] != float('infinity') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # 음수 사이클이 있는지 검사
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] != float('infinity') and distance[u] + weight < distance[v]:
                print("Graph contains negative weight cycle")
                return None

    return distance

graph = {
    'A': [('B', -1), ('C', 4)],
    'B': [('C', 3), ('D', 2), ('E', 2)],
    'C': [],
    'D': [('B', 1), ('C', 5)],
    'E': [('D', -3)]
}

start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)
if distances:
    print("Vertex Distances from start vertex", start_vertex)
    for vertex in distances:
        print(f"Distance to {vertex}: {distances[vertex]}")
