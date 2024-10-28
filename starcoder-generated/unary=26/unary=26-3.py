
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 1, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 > 0
        v3 = v1 * -self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model
negative_slope = float(torch.tensor([0.2]))
m = Model(negative_slope)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
