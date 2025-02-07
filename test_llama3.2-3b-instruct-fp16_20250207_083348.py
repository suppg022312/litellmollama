# GenAI Stack Diagram Generator in Python
==============================================

This script uses the Graphviz library to generate a stack diagram from a given list of operations.

## Prerequisites

*   Install the required libraries using pip:
    ```bash
pip install graphviz
```
*   Make sure you have Graphviz installed on your system. You can download it from <https://graphviz.org/download/>

## Code

```python
import graphviz

class StackDiagramGenerator:
    def __init__(self):
        self.dot = graphviz.Digraph()

    def add_operation(self, name, input_ops, output_ops):
        """Add a new operation to the diagram"""
        self.dot.node(name, name)
        for op in input_ops:
            self.dot.edge(op, name)
        for op in output_ops:
            self.dot.edge(name, op)

    def generate_diagram(self, title="Stack Diagram"):
        """Generate the stack diagram"""
        self.dot.format = 'png'
        self.dot.render(title + "_diagram", view=True)


# Example usage
if __name__ == "__main__":
    # Create a new generator
    generator = StackDiagramGenerator()

    # Add operations to the diagram
    generator.add_operation(
        "Add",
        ["Number 1", "Number 2"],
        ["Result"]
    )
    generator.add_operation(
        "Multiply",
        ["Result", "Factor 1"],
        ["Product"]
    )
    generator.add_operation(
        "Divide",
        ["Product", "Factor 2"],
        ["Quotient"]
    )

    # Generate the diagram
    generator.generate_diagram("Math Operations")
```

## How it works

1.  The `StackDiagramGenerator` class is initialized with a Graphviz digraph object.
2.  The `add_operation` method adds a new operation to the diagram, specifying its input and output operations.
3.  The `generate_diagram` method generates the stack diagram as a PNG file.

## Output

The script will generate a PNG file named `<title>_diagram.png`, where `<title>` is the specified title for the diagram. You can modify this behavior by changing the `format` attribute of the `dot` object or the `render` method call.

Note: The code assumes that the input and output operations are represented as node names in the Graphviz digraph.