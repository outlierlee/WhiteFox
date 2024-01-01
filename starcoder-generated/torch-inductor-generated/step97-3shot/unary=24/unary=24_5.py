
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(19, 18, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(18, 15, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(15, 6, 1, stride=1, padding=0)
    def forward(self, x):
        negative_slope = 2.132203
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = v3 > 0
        v5 = v3 * negative_slope
        v6 = torch.where(v4, v3, v5)
        return v6
# Inputs to the model
x1 = torch.randn(3, 19, 34, 32)