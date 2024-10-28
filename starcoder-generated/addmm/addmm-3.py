
class M(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2

# Initializing the model
m = M()

# Inputs to the model
x1 = torch.randn(20, 20)
x2 = torch.randn(20, 20)
inp = torch.ones(20, 20)
