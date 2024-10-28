
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
    
    def forward(self, x1, x2, x3, x4):
        y1 = self.linear(x1)
        y2 = self.linear(x2)
        y3 = self.linear(x3)
        y4 = self.linear(x4)
        z1 = torch.mm(y1, y2)
        z2 = torch.mm(y3, y4)
        z3 = z1 + z2
        return z3

# Initializing the model
mymodel = MyModel()

# Inputs to the model
x1 = torch.randn(1, 10)
x2 = torch.randn(1, 10)
x3 = torch.randn(1, 10)
x4 = torch.randn(1, 10)
