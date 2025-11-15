from collections import deque
from heapq import heappush, heappop

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            stack.append((neighbor, path + [neighbor]))
    return None

def dijkstra(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heappop(pq)
        if node == goal:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heappush(pq, (cost+weight, neighbor, path + [neighbor]))
    return None, float('inf')
