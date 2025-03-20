from collections import deque
from typing import List, Dict, Set


def solution(nodes: List[int], edges: List[List[int]]) -> List[int]:
    graph = {node: set() for node in nodes}
    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)

    count, trees = [0, 0], find_trees(graph)
    for tree in trees:
        root_count, candidate = [0, 0], [None, None]

        for node in tree:
            tree_type = 1 - int(node % 2 == len(graph[node]) % 2)
            root_count[tree_type] += 1
            candidate[tree_type] = node

        if root_count[0] == 1:
            count[0] += 1
        if root_count[1] == 1:
            count[1] += 1

    return count


def find_trees(graph: Dict[int, Set[int]]) -> List[Set[int]]:
    trees, visited = [], set()
    for node in graph:
        if node in visited:
            continue

        tree, queue = {node}, deque([node])
        while queue:
            node = queue.popleft()
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    tree.add(child)
                    queue.append(child)

        trees.append(tree)

    return trees
