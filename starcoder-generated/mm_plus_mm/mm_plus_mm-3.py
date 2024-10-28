
class M(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3

# Initializing the model
model = M()

# Inputs to the model
x1 = torch.randn(10, 20)
x2 = torch.randn(20, 30)
x3 = torch.randn(10, 20)
x4 = torch.randn(20, 30)
