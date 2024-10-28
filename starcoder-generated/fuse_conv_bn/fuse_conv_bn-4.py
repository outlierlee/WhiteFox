
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3, bias=False)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        v = self.conv(x1)
        v = self.bn(v)
        return v

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 1, 3, 3)
