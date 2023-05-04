# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* First member (email)
* Kevin Chau (kevinch@udel.edu)
* Third member (email)
* Fourth member (email)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# First Problem Title

**Informal Description**: Hey there Runescape Player! We're giving away 7 million GP to the person who can visit all the cities we've listed in the least number of steps! Be wary, some people may repeat steps or are redundant in the way they do things. Can you top the leaderboard? Good luck and best wishes!

> **Formal Description**:
>  * Input: An unweighted and undirected graph G = (V,E) that consists of 22 nodes(cities) that the player will have to visit throughout their journey.
>  * Output: The number of steps it took to visit all the cities in the end and a list referring to what traversal the player will need to make to top the leaderboards.

**Graph Problem/Algorithm**: BFS


**Setup code**:

```python
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
```

**Visualization**:

![bfsOSRS.png](src/bfsOSRS.png)

**Solution code:**

```python
traversed = nx.bfs_edges(G, source="Lumbridge")
bfs = list(traversed)
print("It took " + str(len(bfs)) + " visits to visit all the specified towns in the tournament!")
print("This is the path you should explore to win!: "+ str(bfs))
```

**Output**

```
It took 21 visits to visit all the specified towns in the tournament!
This is the path you should explore to win!: [('Lumbridge', 'Varrock'), ('Lumbridge', 'AlKharid'), ('Lumbridge', 'DraynorVillage'), ('Varrock', 'Edgeville'), ('Varrock', 'GrandExchange'), ('Varrock', 'Digsite'), ('Varrock', 'Falador'), ('AlKharid', 'DuelArena'), ('DraynorVillage', 'PortSarim'), ('DraynorVillage', 'Ardougne'), ('Edgeville', 'BarbarianVillage'), ('PortSarim', 'Rimmington'), ('PortSarim', 'MusaPoint'), ('BarbarianVillage', 'WestArdougne'), ('MusaPoint', 'Karamja'), ('WestArdougne', 'EastArdougne'), ('EastArdougne', 'Yanille'), ('Yanille', 'Catherby'), ('Catherby', 'SeersVillage'), ('Catherby', 'Taverley'), ('SeersVillage', 'Camelot')]

```

**Interpretation of Results**:
The output shows the minimum number of steps needed to visit every single city in the end and the path the player should take to top the leaderboards. Since BFS looks for the shortest path between each city, the algorithm focuses on minimizing the number of steps (including repetitions) to visit all the cities in the end. With 22 cities, the best result is 21 steps which means we've made no repetitions or mistakes. However, realistically, no one would be perfect and would most likely have to make more than 21 visits.
