
class M(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)
        t2 = torch.cat([t1]*3, 1)
        return t2

# Initializing the model
m = M()

# Inputs to the model
x1 = torch.randn(8, 2)
x2 = torch.randn(2, 4)

