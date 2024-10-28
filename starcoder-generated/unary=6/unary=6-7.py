
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        y1 = self.conv(x1)
        y2 = y1 + 3
        y3 = torch.clamp(y2, min=0)
        y4 = torch.clamp(y3, max=6)
        y5 = y1 * y4
        y6 = y5 / 6
        return y6

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
