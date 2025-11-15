import pickle
from graph_builder import build_graph

graph = build_graph("gis_osm_roads_free_1.shp")
with open("graph.pkl", "wb") as f:
    pickle.dump(graph, f)
print("Graph saved to graph.pkl")
