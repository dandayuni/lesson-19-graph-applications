import networkx as nx
import matplotlib.pyplot as plt

abilities = ["Bash", "Double\nBash", "Charge", "Uppercut", "War\nScream", "Heavy\nImpact", "Quadruple\nBash", "Fireworks", "Flyby\nJab", 
             "Flaming\nUppercut", "Half-Moon\nSwipe", "Generalist", "Counter", "Mantle\nof the\nBovemists", "Bak'al's\nGrasp", "Aerodynamics", 
             "Provoke", "Air\nShout", "Enraged\nBlow", "Flying\nKick", "Manachism", "Boiling\nBlood", "Ragnarokkr", "Intoxicating\nBlood", 
             "Collide", "Rejuvinating\nSkin", "Comet", "Whirlwind\nStrike", "Mythril\nSkin", "Shield\nStrike", "Sparkling\nHope", "Armor\nBreaker", 
             "Massive\nBash", "Tempest", "Massacre", "Radiance", "Discombobulate", "Cyclone", "Thunderclap", "Second\nChance", "Blood\nPact", 
             "Hemorrhage", "Brink of\nMadness", "Martyr"]

edges = [("Bash", "Double\nBash", 2), ("Double\nBash", "Charge", 1), ("Charge", "Uppercut", 2), ("Charge", "War\nScream", 2), ("War\nScream", "Uppercut", 2), 
         ("Heavy\nImpact", "Uppercut", 1), ("Uppercut", "Fireworks", 3), ("War\nScream", "Fireworks", 4), ("Uppercut", "Quadruple\nBash", 3), 
         ("War\nScream", "Flyby\nJab", 3), ("War\nScream", "Flaming\nUppercut", 3), ("War\nScream", "Half-Moon\nSwipe", 4), ("Uppercut", "Half-Moon\nSwipe", 4), 
         ("Half-Moon\nSwipe", "Counter", 2),  ("Counter", "Generalist", 2), ("Flyby\nJab", "Mantle\nof the\nBovemists", 3), ("Flaming\nUppercut", "Mantle\nof the\nBovemists", 3), 
         ("Quadruple\nBash", "Bak'al's\nGrasp", 2), ("Fireworks", "Bak'al's\nGrasp", 2), ("Bak'al's\nGrasp", "Flying\nKick", 5), ("Bak'al's\nGrasp", "Enraged\nBlow", 3), 
         ("Bak'al's\nGrasp", "Aerodynamics", 4), ("Counter", "Flying\nKick", 3), ("Counter", "Enraged\nBlow", 5), ("Counter", "Aerodynamics", 3), 
         ("Mantle\nof the\nBovemists", "Provoke", 2), ("Provoke", "Aerodynamics", 2), ("Provoke", "Air\nShout", 2), ("Provoke", "Manachism", 2), 
         ("Aerodynamics", "Flying\nKick", 3), ("Aerodynamics", "Enraged\nBlow", 5), ("Manachism", "Flying\nKick", 3), ("Enraged\nBlow", "Boiling\nBlood", 2), 
         ("Flying\nKick", "Ragnarokkr", 2), ("Boiling\nBlood", "Ragnarokkr", 2), ("Ragnarokkr", "Intoxicating\nBlood", 2), ("Ragnarokkr", "Comet", 2), 
         ("Flying\nKick", "Collide", 3), ("Flying\nKick", "Rejuvinating\nSkin", 4), ("Flying\nKick", "Whirlwind\nStrike", 3), ("Manachism", "Collide", 4), 
         ("Manachism", "Rejuvinating\nSkin", 3), ("Manachism", "Whirlwind\nStrike", 5), ("Boiling\nBlood", "Whirlwind\nStrike", 4), ("Boiling\nBlood", "Armor\nBreaker", 3), 
         ("Boiling\nBlood", "Massive\nBash", 3), ("Rejuvinating\nSkin", "Mythril\nSkin", 2), ("Shield\nStrike", "Mythril\nSkin", 2), ("Shield\nStrike", "Sparkling\nHope", 2), 
         ("Mythril\nSkin", "Sparkling\nHope", 2), ("Massive\nBash", "Tempest", 2),("Massive\nBash", "Massacre", 2), ("Massive\nBash", "Blood\nPact", 3), 
         ("Whirlwind\nStrike", "Tempest", 3), ("Whirlwind\nStrike", "Armor\nBreaker", 3), ("Whirlwind\nStrike", "Armor\nBreaker", 4), ("Whirlwind\nStrike", "Cyclone", 4), 
         ("Whirlwind\nStrike", "Radiance", 3), ("Tempest", "Cyclone", 4), ("Tempest", "Radiance", 4), ("Shield\nStrike", "Radiance", 3), ("Sparkling\nHope", "Radiance", 3), 
         ("Shield\nStrike", "Second\nChance", 3), ("Sparkling\nHope", "Second\nChance", 3), ("Radiance", "Second\nChance", 3), ("Cyclone", "Discombobulate", 3), 
         ("Cyclone", "Thunderclap", 2), ("Blood\nPact", "Hemorrhage", 2), ("Blood\nPact", "Brink of\nMadness", 2), ("Second\nChance", "Martyr", 2), 
         ("Second\nChance", "Brink of\nMadness", 3)]

G = nx.Graph()
G.add_nodes_from(abilities)
G.add_weighted_edges_from(edges)

MST = nx.minimum_spanning_tree(G, algorithm="prim")
pos = nx.spring_layout(G)

nx.draw_networkx(
    G,
    pos, 
    node_size=800,
    node_shape='o',
    font_size=8,
    font_color='black',
    edge_color='gray',
    width=1,
    style='solid',
    with_labels=True
    )

cost = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edges(
    MST, 
    pos, 
    edge_color='red',
    style='dashed', 
    width=2
    )

nx.draw_networkx_edge_labels(
    G, 
    pos, 
    edge_labels=cost,
    label_pos=0.5, 
    font_size=7,
    font_color="blue",
    horizontalalignment="center", 
    verticalalignment="top",
    rotate=True, 
    clip_on=True
    )
        
plt.show()
print(MST)
print("Edges and their weights:")
for edge, weight in cost.items():
    print(f"{edge}, {weight}")