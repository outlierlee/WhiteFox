
class Model(torch.nn.Module):
    def __init__(self, min_value = -1, max_value = 1):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3

# Initializing the model
m = Model(-0.5, 0.5)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
