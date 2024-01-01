
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1
        x2 = v1 - 0.5
        v3 = v1 - x2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randn(10, 3, 64, 64)