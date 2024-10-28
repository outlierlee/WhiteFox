
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.nn.functional.full

    def forward(self, arg1, arg2, dtype, layout, device):
        t1 = self.full([arg1, arg2], 1, dtype=dtype, device=device)
        t2 = t1.to(dtype)
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m = Model()

# Inputs to the model
arg1 = 10
arg2 = 10
dtype = torch.float32
layout = torch.strided
device = torch.device('cpu')
