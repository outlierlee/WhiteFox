
```python
# PyTorch model similar to the example above
import torch

# Define a computation
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([6, 7, 8, 9, 10])

# Identical instructions
z1 = torch.add(x, y)
z2 = z1.clone()

# Identical constants
c1 = torch.tensor([1, 2, 3, 4, 5])
c2 = c1.clone()

# Identical iota instructions
i1 = torch.arange(5)
i2 = i1.clone()
```

In this PyTorch model, `z1` and `z2` are identical instructions, `c1` and `c2` are identical constants, and `i1` and `i2` are identical iota instructions. This pattern can trigger the `HloCSE` optimization pass in TensorFlow XLA.