
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 3)
        self.bn = torch.nn.BatchNorm2d(16)

    def forward(self, x):
        return self.bn(self.conv(x))

# Initializing the model and input
m = Model()
x = torch.randn(1, 3, 32, 32)
