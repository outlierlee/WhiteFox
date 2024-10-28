
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, (2, 2))
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x

# Providing the input tensor (using fast tensor creation method, where two arguments are the shape of the tensor and it's random)
x = torch.randn(1, 1, 6, 6)