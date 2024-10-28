
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.addmm(x1, v1, v1)
        v3 = torch.cat([v1, v2], 1)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16)
