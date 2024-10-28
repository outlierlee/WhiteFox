
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = torch.nn.functional.relu(v1)
        v3 = self.linear(x2)
        v4 = torch.nn.functional.relu(v3)
        v5 = torch.mm(v2, v4)
        v6 = torch.cat([v5 for _ in range(5)], dim=-1)
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5)
x2 = torch.randn(1, 5)
