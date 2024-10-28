
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, x2, inp):
        t1 = torch.mm(x1, x2)
        t2 = t1 + inp
        return t2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 64)
x2 = torch.randn(64, 64)
inp = torch.randn(64, 64)
