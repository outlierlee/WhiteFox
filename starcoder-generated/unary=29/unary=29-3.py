
class Model(torch.nn.Module):
    def __init__(self, minimum_value, maximum_value):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(2, 8, 1, stride=2)
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.clamp_min(v1, self.minimum_value)
        v3 = torch.clamp_max(v2, self.maximum_value)
        return v3

# Initializing the model
m = Model(0., 1.)

# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
