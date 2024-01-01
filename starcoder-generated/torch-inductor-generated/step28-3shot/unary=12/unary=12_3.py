
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, (3, 3), padding=1, groups=3)
    def forward(self, x):
        v = self.conv(x)
        v1 = v.mean([2, 3])
        v2 = nn.Sigmoid()(v1)
        v3 = v1*v2
        return v3
# Inputs to the model
x1 = torch.randn(1, 3, 16, 16)