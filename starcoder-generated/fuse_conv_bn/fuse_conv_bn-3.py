
class M(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        return self.bn(self.conv(x))

# Creating the model and input
m = M()
x1 = torch.rand(2, 1, 3, 3)
