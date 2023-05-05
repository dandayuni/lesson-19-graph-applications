# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Joseph Casagrande (joeycasa@udel.edu)
* Kevin Chau (kevinch@udel.edu)
*
*

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




# Skyrim Political Connections 

**Informal Description**: 
Skyrim is a country/region tattered by war between 
the Imperial Legion and the Stormcloaks. The hero 
of the war, the Dragonborn, encounters important 
figures from both sides of the conflict while on 
their way to bringing peace. By the time the war 
concludes, has the Dragonborn met enough people 
to connect him to everyone significant involved 
in the events. (DFS traversal of "friendship" 
graph to find if connected) 

> **Formal Description**:
>  * Input: An unweighted, directed, friendship graph 
representing the Dragonborn and their connections to 
both Imperials and Stormcloaks. Each node is labeled as 
the person's initials (e.g. John Doe would be "JD")

>  * Output: A boolean value that represents whether the 
graph is fully connected or not. If so, a list of node pairs 
(edges) that show the connection between all of the nodes in 
the graph through an edge path. 

**Graph Problem/Algorithm**: [DFS]

**Setup code**:

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

**Visualization**:

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

**Output**

```

True
[('DB', 'GT'), ('GT', 'CM'), ('CM', 'TM'), ('TM', 'LR'), ('LR', 'CC'), ('CC', 'LH'), ('LH', 'LF'), ('LR', 'LS'), ('LS', 'CA'), ('TM', 'AV'), ('CM', 'GM'), ('DB', 'EE'), ('DB', 'HV'), ('HV', 'RL'), ('DB', 'GJ'), ('DB', 'US'), ('US', 'GS'), ('GS', 'YT'), ('YT', 'KW'), ('KW', 'FB'), ('GS', 'GO'), ('GS', 'HH'), ('GS', 'TS'), ('GS', 'KR'), ('GS', 'AF'), ('GS', 'IC'), ('US', 'AO'), ('US', 'TG')]

```

**Interpretation of Results**:

We can officially say that yes, the Dragonborn has met 
a sufficient number of people as he has either a direct 
or indirect connection with every important figure on 
both sides of the Skyrim revolutionary/civil war. In 
technical terms, this means that every node in the graph 
has at least one path of edges that can connect to any other 
node in the graph.

