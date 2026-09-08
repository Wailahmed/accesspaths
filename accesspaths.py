"""Find an access path through a fictional permission graph."""

import json
from collections import deque
from pathlib import Path


def find_path(graph):
    """Return a path with the fewest edges, or None if unreachable."""
    adjacency = {node["id"]: [] for node in graph["nodes"]}
    for edge in graph["edges"]:
        adjacency[edge["from"]].append(edge["to"])

    source = graph["source"]
    target = graph["target"]

    queue = deque([source])
    parents = {source: None}

    while queue:
        current = queue.popleft()

        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return list(reversed(path))

        for neighbour in adjacency[current]:
            if neighbour not in parents:
                parents[neighbour] = current
                queue.append(neighbour)

    return None


def main():
    example = (
        Path(__file__).resolve().parent
        / "examples"
        / "basic_permissions.json"
    )
    with example.open(encoding="utf-8") as file:
        graph = json.load(file)

    path = find_path(graph)

    print(f"Scenario: {graph['name']}")
    if path is None:
        print("No access path found in this model.")
    else:
        print("Access path found:")
        print(" -> ".join(path))
        print(f"Number of edges: {len(path) - 1}")


if __name__ == "__main__":
    main()
