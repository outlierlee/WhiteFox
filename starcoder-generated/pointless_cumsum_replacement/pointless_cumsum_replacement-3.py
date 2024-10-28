
class Model(torch.nn.Module):
    def __init__(self, args):
        super().__init__()
        
    def forward(self, x):
        t1 = torch.full(args[0], 1, dtype=args[1], device=args[2])
        t2 = t1.type(args[1])
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m = Model(((5, 5), torch.float32, 'cpu'))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
