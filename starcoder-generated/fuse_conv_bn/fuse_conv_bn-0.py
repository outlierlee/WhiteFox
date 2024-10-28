
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        x = self.bn(self.conv(x))
        return x

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 2, 2)
