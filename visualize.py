import folium

def show_path(path):
    start = path[0]
    m = folium.Map(location=[start[1], start[0]], zoom_start=13)

    folium.PolyLine(
        locations=[(lat, lon) for lon, lat in path],
        color='blue',
        weight=5,
        opacity=0.7
    ).add_to(m)

    folium.Marker(location=[path[0][1], path[0][0]], popup="Start", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=[path[-1][1], path[-1][0]], popup="Goal", icon=folium.Icon(color='red')).add_to(m)

    m.save("dijkstra_path.html")
    print("Map saved as dijkstra_path.html")
