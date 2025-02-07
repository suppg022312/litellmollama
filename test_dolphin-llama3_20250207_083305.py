Here is an example of how you can use the `networkx` library in Python to create a simple stack diagram for a neural network:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.DiGraph()

# Add nodes
input_layer = ['i1', 'i2']
hidden_layers = ['h1', 'h2']
output_layer = ['o1']

for layer in [input_layer, hidden_layers, output_layer]:
    for node in layer:
        G.add_node(node)

# Add edges (connections)
G.add_edges_from([('i1', 'h1'), ('i2', 'h2')])

# Set positions
pos = {'i1': [0, 0], 'i2': [0, 2],
       'h1': [3, 0], 'h2': [3, 2],
       'o1': [6, 1]}

# Draw the graph
nx.draw(G, pos, with_labels=True, arrows=False)
plt.show()
```