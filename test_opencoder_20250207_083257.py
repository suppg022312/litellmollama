Creating a general AI Stack Diagram involves creating multiple nodes and connecting them. Here is an example using the Graphviz library in Python:

```python
import graphviz

# Initialize a new graph with no directed edges.
g = graphviz.Digraph()

# Add nodes.
g.node('Data Collection')
g.node('Preprocessing & Feature Engineering')
g.node('Model Building & Training')
g.node('Evaluation')
g.node('Deployment')
g.node('Continuous Learning')

# Add directed edges between the nodes to indicate the flow of AI process.
g.edge('Data Collection', 'Preprocessing & Feature Engineering')
g.edge('Preprocessing & Feature Engineering', 'Model Building & Training')
g.edge('Model Building & Training', 'Evaluation')
g.edge('Evaluation', 'Deployment')
g.edge('Deployment', 'Continuous Learning')

# Display the graph.
g.view()
```
This code will generate a simple stack diagram of an AI process. 

Please note that this is a basic version and you can customize your own nodes and edges according to your requirements.

Before running this code, please ensure to install "graphviz" library in python by using pip command:
```python
pip install graphviz
```
