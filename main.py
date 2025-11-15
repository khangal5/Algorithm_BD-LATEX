from graph_builder import build_graph
from algorithms import bfs, dfs, dijkstra
from visualize import show_path

graph = build_graph("gis_osm_roads_free_1.shp")

start = list(graph.keys())[100]
goal = list(graph.keys())[200]

print("Start:", start)
print("Goal:", goal)

bfs_path = bfs(graph, start, goal)
print("\nBFS Path length:", len(bfs_path) if bfs_path else "not found")

dfs_path = dfs(graph, start, goal)
print("DFS Path length:", len(dfs_path) if dfs_path else "not found")

dij_path, cost = dijkstra(graph, start, goal)
print("Dijkstra Path length:", len(dij_path) if dij_path else "not found", " | Cost:", cost)
show_path(dij_path)
