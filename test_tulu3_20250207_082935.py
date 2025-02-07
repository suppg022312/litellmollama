Certainly! Below is a simple Python script that generates a textual representation of a generic artificial intelligence (AI) stack diagram. This diagram represents typical layers found in an AI system, such as data input, pre-processing, feature extraction, model training, and inference.

```python
# Define the structure of the AI stack

class Layer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def create_ai_stack():
    # Create layers
    data_input = Layer("Data Input")
    pre_processing = Layer("Pre-Processing")
    feature_extraction = Layer("Feature Extraction")
    model_training = Layer("Model Training")
    inference = Layer("Inference")

    # Define the stack diagram structure
    ai_stack = [
        data_input,
        pre_processing,
        feature_extraction,
        model_training,
        inference
    ]

    return ai_stack


def print_ai_stack(ai_stack):
    # Print the AI stack diagram
    for idx, layer in enumerate(ai_stack, start=1):
        print(f"Layer {idx}: {layer}")


# Create and print the AI stack
ai_stack = create_ai_stack()
print_ai_stack(ai_stack)

```

This Python script defines an `AIStack` class that organizes different layers of an artificial intelligence system. Each layer is represented by a `Layer` object with a name. The `create_ai_stack` function builds this structure, and the `print_ai_stack` function outputs it in a readable format.

When you run this code, it prints out:

```
Layer 1: Data Input
Layer 2: Pre-Processing
Layer 3: Feature Extraction
Layer 4: Model Training
Layer 5: Inference
```

This textual representation of an AI stack serves as a basic diagram illustrating the flow from data input through various processing stages to making inferences. For visualization purposes, you might want to use graphical tools like `matplotlib` or `pygraphviz` to create more complex and visually appealing diagrams.

Please note that this is a simple illustration and real-world AI systems can be much more complex with additional layers such as evaluation, hyperparameter tuning, deployment, etc., depending on the specific requirements of the application.