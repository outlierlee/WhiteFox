:
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 1, 1)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.bn(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 10, 10)
