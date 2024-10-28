
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=-1., max_value=1.):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

# Initializing the model
m = Model()

# Specifying the minimum and maximum values using keyword arguments
min_value = -0.5
max_value = 0.5

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
