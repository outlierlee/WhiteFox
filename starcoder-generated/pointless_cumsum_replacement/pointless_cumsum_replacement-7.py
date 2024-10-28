
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2, dtype, layout, device):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.dtype = dtype
        self.layout = layout
        self.device = device

    def forward(self):
        x1 = torch.full([self.arg1, self.arg2], 1, dtype=self.dtype, layout=self.layout, device=self.device, pin_memory=False)
        x2 = x1.type(self.dtype)
        x3 = torch.cumsum(x2, 1)
        return x3

# Initializing the model
m = Model(16, 32, torch.float16, torch.strided, torch.device("cpu"))

# Inputs to the model
