
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(6, 3)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1.view(v1.size(0), -1)
        v3 = self.linear(v2)
        v4 = torch.relu(v3)
        return v4

# Initializing the model
m = MyModel()

# Inputs to the model
x1 = torch.randn(1, 2)
x2 = torch.randn(1, 2)
