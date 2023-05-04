# Video Game Graphing

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Joseph Casagrande (joeycasa@udel.edu)
* Second member (email)
* Third member (email)
* Fourth member (email)

This project is based off of video game scenarios, 
features, and statistics converted into graphs with 
corresponding graphing problems to solve.

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

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

![clean graph](\src\skyrimgraph.png)
![nx graph](\src\nxgraph.png)


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

