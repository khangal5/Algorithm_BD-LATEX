import geopandas as gpd
from shapely.geometry import LineString
from math import sqrt

def build_graph(shapefile_path):
    roads = gpd.read_file(shapefile_path)
    print("Замын тоо:", len(roads))

    graph = {}

    for _, row in roads.iterrows():
        geom = row.geometry
        if isinstance(geom, LineString):
            coords = list(geom.coords)
            for i in range(len(coords)-1):
                p1 = coords[i]
                p2 = coords[i+1]

                dist = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

                if p1 not in graph:
                    graph[p1] = []
                graph[p1].append((p2, dist))

                if p2 not in graph:
                    graph[p2] = []
                graph[p2].append((p1, dist))

    print("Графын оройн тоо:", len(graph))
    return graph
