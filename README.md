# Graph Algorithms Implementation

This repository contains Python implementations of two popular graph algorithms: Prim's Algorithm for Minimum Spanning Tree (MST) and Dijkstra's Algorithm for Single Source Shortest Path (SSSP).

## Prim's Algorithm

The `prim_algorithm.py` file implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a given weighted graph. The graph is represented as an adjacency matrix, and the algorithm outputs the edges and their corresponding weights in the MST.

**Usage:**
- Run the script `prim_algorithm.py`.
- Input a starting vertex (a lowercase letter representing the vertex).

## Dijkstra's Algorithm

The `dijkstra_algorithm.py` file implements Dijkstra's algorithm to find the shortest paths from a given source vertex to all other vertices in a weighted graph. The graph is represented using a dictionary of dictionaries, where the outer dictionary represents vertices, and the inner dictionaries represent neighboring vertices and their edge weights.

**Usage:**
- Run the script `dijkstra_algorithm.py`.
- Input a starting vertex (a lowercase letter representing the vertex).
- The algorithm outputs the shortest path distances and the paths to each vertex.



