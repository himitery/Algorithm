from collections import defaultdict, deque
from typing import List, Set, Dict, Tuple


def solution(edges: List[List[int]]) -> List[int]:
    graph, in_degree, out_degree = defaultdict(lambda: list()), defaultdict(int), defaultdict(int)
    nodes = set()

    for src, dest in edges:
        graph[src].append(dest)
        in_degree[dest] += 1
        out_degree[src] += 1
        nodes |= {src, dest}

    created_node, visited = find_start_node(nodes, in_degree, out_degree), set()
    donut_count, bar_count, eight_count = 0, 0, 0

    for start in graph[created_node]:
        if start not in visited:
            donut, bar, eight = detect_graph(start, graph)
            donut_count, bar_count, eight_count = donut_count + donut, bar_count + bar, eight_count + eight

            visited.add(start)

    return [created_node, donut_count, bar_count, eight_count]


def find_start_node(nodes: Set[int], in_degree: Dict[int, int], out_degree: Dict[int, int]) -> int:
    start = 0
    for node in nodes:
        if out_degree[node] >= 2 and in_degree[node] == 0:
            start = node
            break

    return start


def detect_graph(start: int, graph: Dict[int, List[int]]) -> Tuple[int, int, int]:
    queue, components, count = deque([start]), set(), 0

    while queue:
        node = queue.popleft()
        if node in components:
            continue

        components.add(node)
        for next_node in graph[node]:
            count += 1
            queue.append(next_node)

    return (
        int(count == len(components)),
        int(count == len(components) - 1),
        int(count not in [len(components), len(components) - 1]),
    )
