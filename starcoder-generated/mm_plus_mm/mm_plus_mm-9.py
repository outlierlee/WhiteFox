
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
in_size = 4 # Set this number accordingly
x1 = torch.randn(in_size, in_size)
x2 = torch.randn(in_size, in_size)
x3 = torch.randn(in_size, in_size)
x4 = torch.randn(in_size, in_size)
