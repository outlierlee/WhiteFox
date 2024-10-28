
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1 # Subtract 1 from the output of the linear transformation
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5)
other_tensor = 1 # or other_tensor = torch.tensor([1])
