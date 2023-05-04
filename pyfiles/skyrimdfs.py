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

# DFS
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




nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()