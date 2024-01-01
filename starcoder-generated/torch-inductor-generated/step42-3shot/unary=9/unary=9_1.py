
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1):
        v1 = x1 + 3
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0.0, max=6.0)
        v4 = v3 / 6.0
        return v4
# Inputs to the model
x1 = torch.randn(8, 3, 32, 32)