
class Model1(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)
    def forward(self, x1):
        y1 = self.conv(x1)
        y2 = self.bn(y1)
        y3 = self.bn(y2)
        return y3
# Inputs to the model
x1 = torch.randn(1, 3, 4, 4)