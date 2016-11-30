import networkx as nx

G = nx.Graph([
    (1,5),
    (1,4),
    (1,3),
    (1,2),
    (2,3),
    (2,6),
    (2,9),
    (3,4),
    (3,11),
    (3,10),
    (3,6),
    (4,11),
    (4,12),
    (4,5),
    (5,12),
    (5,8),
    (5,9),
    (6,10),
    (6,7),
    (6,9),
    (7,10),
    (7,13),
    (7,8),
    (7,9),
    (8,13),
    (8,12),
    (8,9),
    (10,11),
    (10,13),
    (11,12),
    (11,13),
    (12,13)
    ])


print("edgecount: {}".format(len(G.edges())))

diG = nx.DiGraph(G)
cyclegen = nx.simple_cycles(diG)

counter = 0
for c in cyclegen:
    if len(list(c)) == 4:
        #print(c)
        counter +=1
print (counter)
# we expect 58, 28*2 for merged traingles and 2 for the outer cycle
