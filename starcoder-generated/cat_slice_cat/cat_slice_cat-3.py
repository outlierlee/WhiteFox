
class Model(torch.nn.Module):
    def __init__(self, input_shape=(100, 100)):
        super().__init__()
        self.input_shape = input_shape
 
    def forward(self, *x1):
        v1 = torch.cat(x1, dim=1)
        v2 = v1[:, 0:int(self.input_shape[1])]
        v3 = v2[:, 0:self.input_shape[1] - int(self.input_shape[1])]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model
m = Model((100, 100))

# Inputs to the model
x1 = [torch.randn(1, 100), torch.randn(1, 100)]
