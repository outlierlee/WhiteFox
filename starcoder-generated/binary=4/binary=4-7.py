
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other = other

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2

# Initializing the model with some other tensor
other_tensor = torch.randn(8)
m = Model(other_tensor)

# Inputs to the model
x1 = torch.randn(1, 3)
