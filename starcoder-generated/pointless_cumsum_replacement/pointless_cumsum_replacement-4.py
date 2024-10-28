
class Model(torch.nn.Module):
    def __init__(self, shape, dtype):
        super().__init__()
        self.t1 = torch.full(shape, 1, dtype=dtype)

    def forward(self, x):
        t2 = convert_element_type(self.t1, torch.get_default_dtype())
        t3 = torch.cumsum(t2, 1)
        return t3
        
# Initializing the model
m = Model((10, 20), torch.float32)

# Inputs to the model
x1 = torch.randn(1, 5, 64, 64)
