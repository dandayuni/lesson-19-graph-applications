import networkx as nx
import matplotlib.pyplot as plt

edge_list = [("Lumbridge", "Varrock"), ("Lumbridge", "AlKharid"), ("Lumbridge", "DraynorVillage"), ("Varrock", "Lumbridge"), ("Varrock", "Edgeville"), ("Varrock", "GrandExchange"), ("Varrock", "Digsite"), ("AlKharid", "Lumbridge"),
             ("AlKharid", "DuelArena"), ("DraynorVillage", "Lumbridge"),
             ("DraynorVillage", "PortSarim"), ("DraynorVillage", "Ardougne"),
             ("PortSarim", "DraynorVillage"), ("PortSarim", "Falador"),
             ("PortSarim", "Rimmington"), ("PortSarim", "MusaPoint"),
             ("Falador", "PortSarim"), ("Falador", "Varrock"),
             ("Falador", "BarbarianVillage"), ("BarbarianVillage", "Falador"),
             ("BarbarianVillage", "Edgeville"), ("BarbarianVillage", "WestArdougne"),
             ("Edgeville", "Varrock"), ("Edgeville", "BarbarianVillage"),
             ("WestArdougne", "BarbarianVillage"), ("WestArdougne", "EastArdougne"),
             ("EastArdougne", "WestArdougne"), ("EastArdougne", "Yanille"),
             ("Yanille", "EastArdougne"), ("Yanille", "Catherby"), ("Catherby", "Yanille"),
             ("Catherby", "SeersVillage"), ("Catherby", "Taverley"),
             ("SeersVillage", "Catherby"), ("SeersVillage", "Camelot"),
             ("Camelot", "SeersVillage"), ("MusaPoint", "PortSarim"),
             ("MusaPoint", "Rimmington"), ("MusaPoint", "Karamja"), ("Rimmington", "PortSarim"),
             ("Rimmington", "MusaPoint"), ("Karamja", "MusaPoint")]


G = nx.Graph()
G.add_edges_from(edge_list)
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()

traversed = nx.bfs_edges(G, source="Lumbridge")
bfs = list(traversed)
print("It took " + str(len(bfs)) + " visits to visit all the specified towns in the tournament!")
print("This is the path you should explore to win!: "+ str(bfs))