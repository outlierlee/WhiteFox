
class MyNetwork(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, kernel_size=3, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.bn(v1)
        return v2

# Initializing the model
m = MyNetwork()

# Inputs to the model
x = torch.randn(1, 3, 3, 3)
