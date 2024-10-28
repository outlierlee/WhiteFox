
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(8, 16)

    def forward(self, x):
        v1 = self.fc(x)
        v2 = torch.mm(v1, v1.t())
        v3 = torch.add(x, v2)
        v4 = torch.cat([v2, v3], 1)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 8)
