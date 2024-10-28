
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2, dtype, layout, device):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x):
        t2 = torch.ones_like(self.t1, dtype=x.dtype, layout=x.layout, device=x.device)
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m = Model(2, 3, torch.float32, torch.sparse_coo, torch.device('cpu'))

# Inputs to the model
x = torch.randn([2, 3], device=m.t1.device, dtype=m.t1.dtype, layout=m.t1.layout)
