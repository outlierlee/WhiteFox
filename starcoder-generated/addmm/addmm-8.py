
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(100, 100)
        self.fc1 = torch.nn.Linear(100, 100)
 
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 100)
x2 = torch.randn(100, 64)
inp = torch.randn(64, 100)
