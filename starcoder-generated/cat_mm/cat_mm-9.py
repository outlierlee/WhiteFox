
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1 for _ in range(2*v1.size(-1))], dim=-1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
in_size = 4 # Specify the dimension of the input matrices
x1 = torch.randn(in_size, in_size)
x2 = torch.randn(in_size, in_size)
