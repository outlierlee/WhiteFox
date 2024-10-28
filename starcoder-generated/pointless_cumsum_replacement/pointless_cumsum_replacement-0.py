
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2, dtype, layout, device):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.dtype = dtype
        self.layout = layout
        self.device = device

    def forward(self):
        t1 = torch.full([self.arg1, self.arg2], 1, dtype=self.dtype, layout=self.layout, device=self.device, pin_memory=False)
        t2 = t1.type(self.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m = Model(10, 10, torch.float32, torch.strided, torch.device('cuda'))

# Inputs to the model
