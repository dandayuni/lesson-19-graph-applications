import networkx as nx
import matplotlib.pyplot as plt

places = ["King's Pass", "Dirtmouth", "Forgotten Crossroads", "Greenpath", "Fungal Wastes", "Resting Grounds", "Crystal Peaks", "The Abyss", "Kingdom's Edge", "Ancient Basin", "City of Tears", "Queen's Gardens", "Deepnest", "Fog Canyon", "Howling Cliffs", "The Hive", "Royal Waterways", "White Palace", "Godhome", "Colosseum", "Birthplace", "Isma's Grove"]
edgelist = [("King's Pass", "Dirtmouth", 1), ("Dirtmouth", "King's Pass", 1), ("Dirtmouth", "Forgotten Crossroads", 1), 
            ("Dirtmouth", "Crystal Peaks", 4), ("Forgotten Crossroads", "Greenpath", 3), ("Forgotten Crossroads", "Fungal Wastes", 5), 
            ("Forgotten Crossroads", "Crystal Peaks", 4), ("Forgotten Crossroads", "Resting Grounds", 10), ("Greenpath", "Forgotten Crossroads", 1), 
            ("Greenpath", "Howling Cliffs", 9), ("Greenpath", "Fog Canyon", 7), ("Greenpath", "Queen's Gardens", 10), 
            ("Howling Cliffs", "King's Pass", 2), ("Howling Cliffs", "Dirtmouth", 2),  ("King's Pass", "Howling Cliffs", 1), 
            ("Fog Canyon", "Fungal Wastes", 3), ("Fog Canyon", "Queen's Gardens", 3), ("Fungal Wastes", "City of Tears", 6), 
            ("Fungal Wastes", "Deepnest", 9), ("Fungal Wastes", "Forgotten Crossroads", 1), ("Crystal Peaks", "Resting Grounds", 7), 
            ("Crystal Peaks", "Forgotten Crossroads", 1), ("Resting Grounds", "City of Tears", 3), ("Resting Grounds", "Forgotten Crossroads", 1), 
            ("City of Tears", "Resting Grounds", 1), ("City of Tears", "Ancient Basin", 6), ("City of Tears", "Kingdom's Edge", 4), 
            ("City of Tears", "Fungal Wastes", 1), ("City of Tears", "Royal Waterways", 3), ("Ancient Basin", "The Abyss", 3), 
            ("Ancient Basin", "City of Tears", 3), ("Ancient Basin", "Kingdom's Edge", 1), ("Ancient Basin", "Deepnest", 1), 
            ("Ancient Basin", "White Palace", 3), ("White Palace", "Ancient Basin", 1), ("Kingdom's Edge", "City of Tears", 1), 
            ("Kingdom's Edge", "The Hive", 2), ("Kingdom's Edge", "Ancient Basin", 5), ("Kingdom's Edge", "Colosseum", 6), 
            ("The Hive", "Kingdom's Edge", 1), ("The Abyss", "Birthplace", 1), ("Birthplace", "The Abyss", 1),
            ("The Abyss", "Ancient Basin", 1), ("Colosseum", "Kingdom's Edge", 1), ("Royal Waterways", "City of Tears", 1), 
            ("Royal Waterways", "Isma's Grove", 1), ("Royal Waterways", "Godhome", 5), ("Godhome", "Royal Waterways", 1), 
            ("Isma's Grove", "Royal Waterways", 1), ("Isma's Grove", "City of Tears", 1), ("Queen's Gardens", "Fog Canyon", 1),
            ("Queen's Gardens", "Fungal Wastes", 7), ("Queen's Gardens", "Deepnest", 5), ("Deepnest", "Fungal Wastes", 1), 
            ("Deepnest", "Queen's Gardens", 7), ("Deepnest", "Ancient Basin", 5)]

G = nx.DiGraph()
G.add_nodes_from(places)
G.add_weighted_edges_from(edgelist)

start = "King's Pass"
end = "Resting Grounds"

shortest_path = nx.dijkstra_path(G, start, end)
total_weight = sum([G[shortest_path[i]][shortest_path[i+1]]['weight'] for i in range(len(shortest_path)-1)])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)],
                       edge_color='b', width=3)
plt.axis('off')

print(f"Shortest Path from {start} to {end}: {shortest_path}")
print(f"Total Weight of the Shortest Path from {start} to {end}: {total_weight}")
plt.show()
