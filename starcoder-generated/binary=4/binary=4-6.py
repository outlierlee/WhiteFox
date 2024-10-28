
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 8)
 
    def forward(self, x1, x2):
        v1 = self.lin(x1)
        v2 = v1 + x2
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10)
x2 = torch.randn(10)
