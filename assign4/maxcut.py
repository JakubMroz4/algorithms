
import matplotlib.pyplot as plt
import networkx as nx
import gurobipy as grb
from collections import defaultdict
import matplotlib.cm as cm

# part 1
node_positions = {'s': (0, 1), 'v1': (1, 2), 'v4': (3, 2), 'v3': (2, 1),
       'v2': (1, 0), 'v5': (3, 0), 't': (4, 1)}
edges = {('s', 'v1'):  14, ('s', 'v2'): 25, ('v1', 'v4'): 21, ('v1', 'v3'): 3,
         ('v2', 'v3'): 13, ('v2', 'v5'): 7, ('v3', 'v1'): 6, ('v3', 'v5'): 15,
         ('v4', 'v3'): 10, ('v4', 't'): 20, ('v5', 'v4'): 5, ('v5', 't'): 10}

V = list(node_positions)
E = list(edges)

E_hat = E + [('t', 's')] # add edge t to s with infinite capacity to complete the flow
Vp_hat = defaultdict(set) # vertices neighboring node via entering edges
Vm_hat = defaultdict(set) # vertices neighboring node via exiting edges
for (i, j) in E_hat:
    Vp_hat[j].add(i)
    Vm_hat[i].add(j)

graph = nx.DiGraph()
graph.add_edges_from(E)


# part 2: optimization
maxflow = grb.Model()
x = maxflow.addVars(E_hat)
con_z = maxflow.addConstrs((sum(x[j, i] for j in Vp_hat[i]) - sum(x[i, j] for j in Vm_hat[i]) == 0) for i in V) # sum of incoming and outgoing flow == 0
con_y = maxflow.addConstrs(x[i, j] <= edges[i, j] for (i, j) in E) # Xij <= Cij
maxflow.setObjective(x['t', 's'], grb.GRB.MAXIMIZE)
maxflow.optimize()


# part 3: visualization
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim([-0.25, 4.25])
ax.set_ylim([-0.25, 2.25])

node_size = 2000
edgecolors = 'black'
arrowsize = 15
node_color = "white"
style = "-"
edge_color = [cm.binary(0.1 + 0.9 * x[(i, j)].X / edges[i, j]) for (i, j) in E]
edge_labels = {(i, j): '{}/{}'.format(int(x[i, j].X), edges[i, j]) for (i, j) in E}

nx.draw_networkx(graph, ax=ax, pos=node_positions, nodelist=V, edgelist=[],
                 node_color=node_color, edgecolors=edgecolors,
                 node_size=node_size)
nx.draw_networkx_edges(graph, ax=ax, pos=node_positions, edgelist=E,
                       edge_color=edge_color, style=style,
                       node_size=node_size, arrowsize=arrowsize)
nx.draw_networkx_edge_labels(graph, ax=ax, pos=node_positions, edge_labels=edge_labels)

ax.axis('off')
plt.savefig('maxflow.jpg', dpi=400)