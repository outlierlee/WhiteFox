
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
        self.other = other

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        v3 = torch.nn.functional.ReLU()(v2)
        return v3

# Initializing the model
m = Model(torch.randn(10, 5))

# Inputs to the model
x1 = torch.randn(1, 5)