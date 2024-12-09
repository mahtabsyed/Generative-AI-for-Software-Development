"""
Dijkstra's algorithm
This exercise involves debugging a function that implements Dijkstra's algorithm to calculate the shortest path from node 0 to every other node in a graph and outputs a dictionary with every node and its distance from 0 as well as a boolean saying whether all nodes are reachable or not. The function reads a graph.json file from the local directory to obtain the graph, which is not provided. The graph is expected to consist of exactly 20 nodes.

Instructions: The function's output must remain consistent, retaining the same order.
Constraints: Only libraries that are already imported in the exercise block may be used.

Hints:
1. A helper function exists for deserializing a graph.json. You can request an LLM to outline the structure of the graph in the .json file, ensuring it can be correctly loaded by this function, and to generate some example files for testing.
2. Knowing the graph's structure allows you to ask an LLM to create some graphs fitting this structure, enabling you to test your code with various graphs.
3. Before identifying potential bugs, consider asking an LLM to explain the function's workings.
"""

# I have a graph.json file in my local directory. Can you use that and write tes cases to check all edge cases of this function dijkstra which has bugs I am trying to find.


from collections import defaultdict
import json

## Helper function - Do NOT edit or overwrite it in the solution block.


# Deserialize graph from JSON
# The graph has 20 nodes, numbered 0-19
def deserialize_graph(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return defaultdict(list, {int(k): v for k, v in data.items()})


# Exercise block. Do not add or remove any library and do not add/remove any argument in the function.
import heapq


def dijkstra_fixed(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    all_nodes_visited = len(visited) == len(graph)

    return distances, all_nodes_visited
