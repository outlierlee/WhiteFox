
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, 11)
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 + x1
        return torch.cat([v2, x2])
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 6, 64, 64)