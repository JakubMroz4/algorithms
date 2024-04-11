
import matplotlib.pyplot as plt
import networkx as nx
import gurobipy as grb

# part 1: graph
node_positions = {'s': (0, 1), 'v1': (1, 2), 'v4': (3, 2), 'v3': (2, 1),
       'v2': (1, 0), 'v5': (3, 0), 't': (4, 1)}
edges = {('s', 'v1'):  14, ('s', 'v2'): 25, ('v1', 'v4'): 21, ('v1', 'v3'): 3,
         ('v2', 'v3'): 13, ('v2', 'v5'): 7, ('v3', 'v1'): 6, ('v3', 'v5'): 15,
         ('v4', 'v3'): 10, ('v4', 't'): 20, ('v5', 'v4'): 5, ('v5', 't'): 10}

V = list(node_positions)
E = list(edges)
graph = nx.DiGraph()
graph.add_edges_from(E)


# part 2: optimization

mincut = grb.Model()
y = mincut.addVars(E)
z = mincut.addVars(V, lb=-grb.GRB.INFINITY, ub=grb.GRB.INFINITY)
con_x = mincut.addConstrs(y[i, j] >= z[i] - z[j] for (i, j) in E) # Yij <= Zi - Zj
z['s'].lb = z['s'].ub = 1
z['t'].lb = z['t'].ub = 0
mincut.setObjective(sum(edges[i, j] * y[i, j] for (i, j) in E), grb.GRB.MINIMIZE)
mincut.optimize()


# part 3: visualization
edgecolors = 'black'
node_size = 2000
arrowsize = 15

figure, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim([-0.25, 4.25])
ax.set_ylim([-0.25, 2.25])

style = [(0, (5, 5)) if y[i, j].X == 1 else '-' for (i, j) in E]
node_color = ['cyan' if z[i].X == z['s'].X else 'red' for i in V] # blue if connected to source, else red
edge_color = "black"
edge_labels = {(i, j): '{}/{}'.format(int(con_x[i, j].Pi), edges[i, j]) for (i, j) in E}

nx.draw_networkx(graph, ax=ax, pos=node_positions, nodelist=V, edgelist=[],
                 node_color=node_color, edgecolors=edgecolors,
                 node_size=node_size)

nx.draw_networkx_edges(graph, ax=ax, pos=node_positions, edgelist=E,
                       edge_color=edge_color, style=style,
                       node_size=node_size, arrowsize=arrowsize)

nx.draw_networkx_edge_labels(graph, ax=ax, pos=node_positions, edge_labels=edge_labels)

ax.axis('off')
plt.savefig('mincut.jpg', dpi=400)