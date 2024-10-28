
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 8, 3, stride=1, padding=1)
 
    def forward(self, x1):
        y1 = self.conv(x1)
        y2 = y1 * 0.5
        y3 = y1 * 0.7071067811865476
        y4 = torch.erf(y3)
        y5 = y4 + 1
        y6 = y2 * y5
        return y6

# Initializing the model
n = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 32, 32)
