import pytest
from dijkstra import dijkstra, deserialize_graph


def test_dijkstra_all_nodes_reachable():
    graph = deserialize_graph(
        "/Users/mahtabsyed/Documents/VSCode/Generative AI for Software Development/2_Testing_Documentation/graph.json"
    )
    distances, all_nodes_visited = dijkstra(graph, 0)
    assert all_nodes_visited == True
    assert len(distances) == 20
    assert all(distances[node] != float("infinity") for node in range(20))


def test_dijkstra_some_nodes_unreachable():
    graph = {0: [(1, 1)], 1: [(2, 1)], 2: [], 3: [(4, 1)], 4: []}
    distances, all_nodes_visited = dijkstra(graph, 0)
    assert all_nodes_visited == False
    assert distances[3] == float("infinity")
    assert distances[4] == float("infinity")


def test_dijkstra_correct_distances():
    graph = {0: [(1, 1), (2, 4)], 1: [(2, 2), (3, 5)], 2: [(3, 1)], 3: []}
    distances, all_nodes_visited = dijkstra(graph, 0)
    assert distances[0] == 0
    assert distances[1] == 1
    assert distances[2] == 3
    assert distances[3] == 4


def test_dijkstra_single_node_graph():
    graph = {0: []}
    distances, all_nodes_visited = dijkstra(graph, 0)
    assert all_nodes_visited == True
    assert distances[0] == 0


def test_dijkstra_disconnected_graph():
    graph = {0: [(1, 1)], 1: [(2, 1)], 2: [], 3: [(4, 1)], 4: []}
    distances, all_nodes_visited = dijkstra(graph, 0)
    assert all_nodes_visited == False
    assert distances[3] == float("infinity")
    assert distances[4] == float("infinity")


if __name__ == "__main__":
    pytest.main()
