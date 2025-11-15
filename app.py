from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import math

app = Flask(__name__)
CORS(app)

with open("graph.pkl", "rb") as f:
    graph = pickle.load(f)

# ===== Algorithms =====
def bfs(graph, start, goal):
    from collections import deque
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
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
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

def dijkstra(graph, start, goal):
    import heapq
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == goal:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, w in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (cost+w, neighbor, path+[neighbor]))
    return None, None

def nearest_node(graph, point):
    px, py = point[1], point[0]  # Graph нь (lon, lat) байна гэж үзэв
    nearest = min(graph.keys(), key=lambda n: (n[0]-px)**2 + (n[1]-py)**2)
    return nearest

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/find_path", methods=["GET"])
def find_path():
    start_coord = tuple(map(float, request.args.get("start").split(",")))
    goal_coord  = tuple(map(float, request.args.get("goal").split(",")))
    algo = request.args.get("algo", "dijkstra")

    start_node = nearest_node(graph, start_coord)
    goal_node  = nearest_node(graph, goal_coord)
    print("Start:", start_node, "Goal:", goal_node)

    if algo == "bfs":
        path = bfs(graph, start_node, goal_node)
        cost = len(path) if path else None
    elif algo == "dfs":
        path = dfs(graph, start_node, goal_node)
        cost = len(path) if path else None
    else:
        path, cost = dijkstra(graph, start_node, goal_node)

    return jsonify({"path": path, "cost": cost})

if __name__ == "__main__":
    app.run(debug=True)
