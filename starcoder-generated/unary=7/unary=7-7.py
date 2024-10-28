
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp(v1 + 3, min=0, max=6)
        v3 = v1 * v2
        v4 = v3 / 6
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3)
