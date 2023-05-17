# CISC320 Spring 2023 Lesson 19 - Graph Applications

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Joseph Casagrande (joeycasa@udel.edu)
* Kevin Chau (kevinch@udel.edu)
* Ray Yang (Doomsucc@udel.edu)
* Daniel Xu (dxu@udel.edu)

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

**Informal Description:** Hey there Runescape Player! We're giving away 7 million GP to the person who can visit all the cities we've listed in the least number of steps! Be wary, some people may repeat steps or are redundant in the way they do things. Can you top the leaderboard? Good luck and best wishes!

> **Formal Description:**
>  * Input: An unweighted and undirected graph G = (V,E) that consists of 22 nodes(cities) that the player will have to visit throughout their journey.
>  * Output: The number of steps it took to visit all the cities in the end and a list referring to what traversal the player will need to make to top the leaderboards.

**Graph Problem/Algorithm:** BFS


**Setup code:**

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

**Visualization:**

![bfsOSRS.png](src/bfsOSRS.png)

**Solution code:**

```python
traversed = nx.bfs_edges(G, source="Lumbridge")
bfs = list(traversed)
print("It took " + str(len(bfs)) + " visits to visit all the specified towns in the tournament!")
print("This is the path you should explore to win!: "+ str(bfs))
```

**Output:**

```
It took 21 visits to visit all the specified towns in the tournament!
This is the path you should explore to win!: [('Lumbridge', 'Varrock'), ('Lumbridge', 'AlKharid'), ('Lumbridge', 'DraynorVillage'), ('Varrock', 'Edgeville'), ('Varrock', 'GrandExchange'), ('Varrock', 'Digsite'), ('Varrock', 'Falador'), ('AlKharid', 'DuelArena'), ('DraynorVillage', 'PortSarim'), ('DraynorVillage', 'Ardougne'), ('Edgeville', 'BarbarianVillage'), ('PortSarim', 'Rimmington'), ('PortSarim', 'MusaPoint'), ('BarbarianVillage', 'WestArdougne'), ('MusaPoint', 'Karamja'), ('WestArdougne', 'EastArdougne'), ('EastArdougne', 'Yanille'), ('Yanille', 'Catherby'), ('Catherby', 'SeersVillage'), ('Catherby', 'Taverley'), ('SeersVillage', 'Camelot')]

```

**Interpretation of Results:**
The output shows the minimum number of steps needed to visit every single city in the end and the path the player should take to top the leaderboards. Since BFS looks for the shortest path between each city, the algorithm focuses on minimizing the number of steps (including repetitions) to visit all the cities in the end. With 22 cities, the best result is 21 steps which means we've made no repetitions or mistakes. However, realistically, no one would be perfect and would most likely have to make more than 21 visits.




# Skyrim Political Connections 

**Informal Description:**
Skyrim is a country/region tattered by war between 
the Imperial Legion and the Stormcloaks. The hero 
of the war, the Dragonborn, encounters important 
figures from both sides of the conflict while on 
their way to bringing peace. By the time the war 
concludes, has the Dragonborn met enough people 
to connect him to everyone significant involved 
in the events. (DFS traversal of "friendship" 
graph to find if connected) 

> **Formal Description:**
>  * Input: An unweighted, directed, friendship graph 
representing the Dragonborn and their connections to 
both Imperials and Stormcloaks. Each node is labeled as 
the person's initials (e.g. John Doe would be "JD")

>  * Output: A boolean value that represents whether the 
graph is fully connected or not. If so, a list of node pairs 
(edges) that show the connection between all of the nodes in 
the graph through an edge path. 

**Graph Problem/Algorithm:** [DFS]

**Setup code:**

```python

import networkx as nx
import matplotlib.pyplot as plt

people = ["DB", "GT", "TM", "CM", "GM", "CC", "EE", "LR", "HV", "LF", "LH", "LS" ,
          "CA", "AV", "GJ", "RL", "US", "GS", "YT", "KW", "GO", "FB", "HH", "TS",
          "KR", "AF", "IC", "TG", "AO"]
edgelist = [("DB","GT"), ("DB","CM"), ("DB","CC"), ("DB","EE"), ("DB","LR"), ("DB","HV"),
            ("GT","CM"), ("GT","TM"), ("GT","LR"), ("GT","CA"), ("TM","CM"), ("TM","LR"),
            ("TM","AV"), ("CM","GM"), ("LR","CC"), ("LR","LF"), ("LR","LH"), ("LR","LS"),
            ("LR","CA"), ("HV","RL"), ("LH","CC"), ("LH","LF"), ("CA","LS"), ("DB","GJ"),
            ("DB","RL"), ("DB","US"), ("DB","AO"), ("DB","GS"), ("DB","TG"), ("US","GS"),
            ("US","AO"), ("US","TG"), ("GS","YT"), ("GS","KW"), ("GS","GO"), ("GS","FB"),
            ("GS","HH"), ("GS","TS"), ("GS","KR"), ("GS","AF"), ("GS","IC"), ("KW","YT"),
            ("KW","FB")]

G = nx.Graph()
G.add_nodes_from(people)
G.add_edges_from(edgelist)

```

**Visualization:**

![clean graph](src/skyrimgraph.png)
![nx graph](src/nxgraph.png)


**Solution code:**

```python

dfs_edges = nx.dfs_edges(G, source="DB")

final_edges = []
final_people = []

for edge in dfs_edges:
    final_edges.append(edge)
    for node in edge:
        final_people.append(node)

verdict = ""
for person in people:
    if person not in final_people:
        verdict = False
        break
    verdict = True
print(verdict)

if verdict:
    print(final_edges)

```

**Output:**

```

True
[('DB', 'GT'), ('GT', 'CM'), ('CM', 'TM'), ('TM', 'LR'), ('LR', 'CC'), ('CC', 'LH'), ('LH', 'LF'), ('LR', 'LS'), ('LS', 'CA'), ('TM', 'AV'), ('CM', 'GM'), ('DB', 'EE'), ('DB', 'HV'), ('HV', 'RL'), ('DB', 'GJ'), ('DB', 'US'), ('US', 'GS'), ('GS', 'YT'), ('YT', 'KW'), ('KW', 'FB'), ('GS', 'GO'), ('GS', 'HH'), ('GS', 'TS'), ('GS', 'KR'), ('GS', 'AF'), ('GS', 'IC'), ('US', 'AO'), ('US', 'TG')]

```

**Interpretation of Results:**

We can officially say that yes, the Dragonborn has met 
a sufficient number of people as he has either a direct 
or indirect connection with every important figure on 
both sides of the Skyrim revolutionary/civil war. In 
technical terms, this means that every node in the graph 
has at least one path of edges that can connect to any other 
node in the graph.




# Hollow Knight

**Informal Description:**
In the world of Hollow Knight there are many paths to get lost upon. There are also many paths to reach the same places. This allows us to ask, what is the fastest way to get to Dream Nail.

> **Formal Description:**
> Input: A weighted, directed distance graph for all the ways to get to Resting Grounds (Where Dream Nail is Obtained).
> Output: The shortest distance to Resting Grounds measured by how many transitions there are.

**Graph Problem/Algorithm:** 
SSSP

**Setup code:**
```python
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

nx.draw(G, with_labels=True, node_color='lightblue')
plt.show()
```
**Visualization:**
![Hollow Knight Map](src/HKMap.png)
![Hollow Knight Map With Weighted Edges](src/HKMapWithWeights.png)

**Solution Code:**
```python
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
```

**Output:**
Shortest Path from King's Pass to Resting Grounds: ["King's Pass", 'Dirtmouth', 'Forgotten Crossroads', 'Resting Grounds']
Total Weight of the Shortest Path from King's Pass to Resting Grounds: 12

**Interpretation of Results:**
This means that based on number of transitions, the best path is from King's Pass, to Dirtmouth, to Forgotten Crossroads, to Resting Grounds. This is consistent with the actual game's fastest path since in speedruns runners would go to Blue Lake from Salubra's by doing a shade skip. The way I mapped it was if you took Tram Pass there though so it's not fully consistent. Making a graph of transitions is difficult to accurately say how long going somewhere may take though since the starting position changes depending on where you enter from. I made this by doing the most common routing that a beginner would probably take. The number of total transitions would be higher in the actual speedrun since they need to do other things to complete the game (i.e. get VS, dash, claw), rather then just trying to instantly get dream nail. This graph is also not the best representation of speed since the size of rooms aren't consistent, so some sections like Deepnest have very large rooms and few transitions, but others like Forgotten Crossroads has many transitions and smaller rooms.

# Wynncraft Warrior Ability Tree

**Informal Description:**
Wynncraft is an MMORPG that allows the player to select from five classes to play. One of these classes is the warrior, a fierce melee character that uses a spear as his main weapon. 
This class has an ability tree that augments the characters abilities. How can the player unlock every ability in the tree using the least amount of ability points possible?

> **Formal Description:**
> Input: A weighted, fully connected graph that contains all the major ability nodes in the warrior ability tree.
> Output: A minimum spanning tree that connected all the abilities using the least number of ability points possible.

**Graph Problem/Algorithm:** 
Minimum Spanning Tree (Prim)

**Setup code:**
```python
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

```
**Visualization:**
![Warrior Skill Tree](src/warrior_skill_tree.png)

**Solution Code:**
```python
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
```

**Output:**
Graph with 44 nodes and 43 edges
Edges and their weights:
('Bash', 'Double\nBash'), 2
('Double\nBash', 'Charge'), 1
('Charge', 'Uppercut'), 2
('Charge', 'War\nScream'), 2
('Uppercut', 'War\nScream'), 2
('Uppercut', 'Heavy\nImpact'), 1
('Uppercut', 'Fireworks'), 3
('Uppercut', 'Quadruple\nBash'), 3
('Uppercut', 'Half-Moon\nSwipe'), 4
('War\nScream', 'Fireworks'), 4
('War\nScream', 'Flyby\nJab'), 3
('War\nScream', 'Flaming\nUppercut'), 3
('War\nScream', 'Half-Moon\nSwipe'), 4
('Quadruple\nBash', "Bak'al's\nGrasp"), 2
('Fireworks', "Bak'al's\nGrasp"), 2
('Flyby\nJab', 'Mantle\nof the\nBovemists'), 3
('Flaming\nUppercut', 'Mantle\nof the\nBovemists'), 3
('Half-Moon\nSwipe', 'Counter'), 2
('Generalist', 'Counter'), 2
('Counter', 'Flying\nKick'), 3
('Counter', 'Enraged\nBlow'), 5
('Counter', 'Aerodynamics'), 3
('Mantle\nof the\nBovemists', 'Provoke'), 2
("Bak'al's\nGrasp", 'Flying\nKick'), 5
("Bak'al's\nGrasp", 'Enraged\nBlow'), 3
("Bak'al's\nGrasp", 'Aerodynamics'), 4
('Aerodynamics', 'Provoke'), 2
('Aerodynamics', 'Flying\nKick'), 3
('Aerodynamics', 'Enraged\nBlow'), 5
('Provoke', 'Air\nShout'), 2
('Provoke', 'Manachism'), 2
('Enraged\nBlow', 'Boiling\nBlood'), 2
('Flying\nKick', 'Manachism'), 3
('Flying\nKick', 'Ragnarokkr'), 2
('Flying\nKick', 'Collide'), 3
('Flying\nKick', 'Rejuvinating\nSkin'), 4
('Flying\nKick', 'Whirlwind\nStrike'), 3
('Manachism', 'Collide'), 4
('Manachism', 'Rejuvinating\nSkin'), 3
('Manachism', 'Whirlwind\nStrike'), 5
('Boiling\nBlood', 'Ragnarokkr'), 2
('Boiling\nBlood', 'Whirlwind\nStrike'), 4
('Boiling\nBlood', 'Armor\nBreaker'), 3
('Boiling\nBlood', 'Massive\nBash'), 3
('Ragnarokkr', 'Intoxicating\nBlood'), 2
('Ragnarokkr', 'Comet'), 2
('Rejuvinating\nSkin', 'Mythril\nSkin'), 2
('Whirlwind\nStrike', 'Tempest'), 3
('Whirlwind\nStrike', 'Armor\nBreaker'), 4
('Whirlwind\nStrike', 'Cyclone'), 4
('Whirlwind\nStrike', 'Radiance'), 3
('Mythril\nSkin', 'Shield\nStrike'), 2
('Mythril\nSkin', 'Sparkling\nHope'), 2
('Shield\nStrike', 'Sparkling\nHope'), 2
('Shield\nStrike', 'Radiance'), 3
('Shield\nStrike', 'Second\nChance'), 3
('Sparkling\nHope', 'Radiance'), 3
('Sparkling\nHope', 'Second\nChance'), 3
('Massive\nBash', 'Tempest'), 2
('Massive\nBash', 'Massacre'), 2
('Discombobulate', 'Cyclone'), 3
('Second\nChance', 'Martyr'), 2

**Interpretation of Results:**
This shows how the player can unlock every major ability using the least number of ability points. Starting from the root node, Bash, the player can follow the tree and select the edges that are outlined in the output as well as the cost of each of those edges so that the player is able to know how many points they will need to acquire as they level up before they can unlock the next major node. Most video games will tend to limit the amount of ability points that the player is given so that you have to make a strategic decision between different nodes and what kind of 'build' that the player is going for. I thought it would be interesting to see if the player was given an unlimited amount of points, what would be the most efficient way to connect all of the nodes.