
class Model(torch.nn.Module):
    def __init__(self, arg1=10, arg2=20, dtype=torch.float32, layout=torch.strided, device=torch.device('cpu')):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.dtype = dtype
        self.layout = layout
        self.device = device

    def forward(self):
        t1 = torch.full([self.arg1, self.arg2], 1, dtype=self.dtype, layout=self.layout, device=self.device, pin_memory=False)
        t2 = t1.to(dtype=self.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m = Model()
