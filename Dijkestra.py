
import heapq


def dijkstra(graph, source):
    # Initialize distances with infinity for all vertices except the source
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Initialize an empty dictionary to store the shortest path to each vertex
    shortest_paths = {}

    # Initialize a priority queue to store vertices and their tentative distances
    pq = [(0, source)]
    shortest_paths[source] = source

    while pq:
        # Pop the vertex with the smallest tentative distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip if we have already processed this vertex
        if current_distance > distances[current_vertex]:
            continue

        # Update the distances and shortest paths to the neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance and shortest path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = current_vertex

                # Add the neighboring vertex to the priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances, shortest_paths


graph = {
    's': {
        't': 10,
        'y': 5,
    },
    't': {
        'y': 2,
        'x': 1,
    },
    'x': {
        'z': 7,
    },
    'z': {
        'x': 6,
        's': 7,
    },
    'y': {
        'z': 2,
        'x': 9,
        't': 3,
    },
}

print("\nSecond............Dijkstra's Algorithm\n")

restart_dijkstra = True

while restart_dijkstra:
    beginning = input("Enter beginning vertex: ")

    distances, shortest_paths = dijkstra(graph, beginning)

    print("\nCurrent | Previous | Shortest path")
    print(" vertex |  vertex  |   to vertex")
    print("--------|----------|---------------")

    for vertex in graph:
        print(f"    {vertex}   |    {shortest_paths[vertex]}     |      {distances[vertex]}")

    where_next = input("\nEnter 1 to restart Dijkstra's Algorithm, Enter 2 to end program: ")
    if where_next != '1':
        restart_dijkstra = False
