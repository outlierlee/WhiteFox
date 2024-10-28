
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2, dtype, layout=None, device=None):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.dtype = dtype
        self.layout = layout
        self.device = device

    def forward(self):
        t1 = torch.full([self.arg1, self.arg2], 1, dtype=self.dtype, device=self.device, layout=self.layout)
        t2 = t1.to(dtype=self.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m = Model(3, 4, torch.float32, layout=torch.strided, device=torch.device('cpu'))

# Inputs to the model
