"""Behavioural tests for permission-path discovery."""

import unittest

from accesspaths import find_path


def make_graph(edges, source="start", target="target"):
    """Build a small directed graph for a test."""
    node_ids = {source, target}
    for start, end in edges:
        node_ids.update((start, end))

    return {
        "nodes": [{"id": node} for node in sorted(node_ids)],
        "edges": [
            {"from": start, "to": end}
            for start, end in edges
        ],
        "source": source,
        "target": target,
    }


class FindPathTests(unittest.TestCase):
    def test_connected_chain(self):
        graph = make_graph([
            ("start", "script"),
            ("script", "service"),
            ("service", "target"),
        ])
        self.assertEqual(
            find_path(graph),
            ["start", "script", "service", "target"],
        )

    def test_broken_chain(self):
        graph = make_graph([
            ("script", "service"),
            ("service", "target"),
        ])
        self.assertIsNone(find_path(graph))

    def test_permissions_are_directional(self):
        graph = make_graph([("target", "start")])
        self.assertIsNone(find_path(graph))

    def test_cycle_without_route_to_target(self):
        graph = make_graph([
            ("start", "service"),
            ("service", "start"),
        ])
        self.assertIsNone(find_path(graph))

    def test_finds_shortest_route_by_edge_count(self):
        graph = make_graph([
            ("start", "a"),
            ("a", "b"),
            ("b", "target"),
            ("start", "shortcut"),
            ("shortcut", "target"),
        ])
        self.assertEqual(
            find_path(graph),
            ["start", "shortcut", "target"],
        )

    def test_alternative_route_survives_removal(self):
        graph = make_graph([
            ("start", "a"),
            ("a", "target"),
            ("start", "b"),
            ("b", "target"),
        ])
        graph["edges"] = [
            edge for edge in graph["edges"]
            if (edge["from"], edge["to"]) != ("start", "a")
        ]
        self.assertEqual(
            find_path(graph),
            ["start", "b", "target"],
        )

    def test_source_is_already_target(self):
        graph = make_graph([], source="target", target="target")
        self.assertEqual(find_path(graph), ["target"])


if __name__ == "__main__":
    unittest.main()
