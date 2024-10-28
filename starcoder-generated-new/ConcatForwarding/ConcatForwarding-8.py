

Create a class Model defines two methods, setup() and forward(). The method 'setup' will initialize all the required layers and operations. The method 'forward' will perform a forward pass on the network.

1. Define the 'setup' method.

```python
def setup(self, axis, shapes_list):
    self.concat1 = tf.keras.layers.Concatenate(axis=axis)
    self.concat2 = tf.keras.layers.Concatenate(axis=axis)
```

2. The forward pass method takes a list of tensors (A, B, and C) as the input.

```python
def forward(self, tensors):
    A, B, C = tensors
    t1 = self.concat1([A, B])
    final_model = self.concat2([t1, C])
    return final_model
```

# Usage

Initialize the model with necessary inputs (axis for concatenate and shape of tensors A, B, and C).

```python
model = Model()
axis = 1
A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])
C = tf.constant([[0, 9], [0, 10]])

# Setup and Forward pass
model.setup(axis, [A.shape, B.shape, C.shape])
output = model.forward([A, B, C])
```