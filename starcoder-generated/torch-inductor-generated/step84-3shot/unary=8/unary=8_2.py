
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(128, 128, 5, stride=2, padding=1, bias=False)
        self.conv1 = torch.nn.Conv2d(128, 256, 1)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        v7 = self.conv1(v6)
        return v7
# Inputs to the model
x1 = torch.randn(1, 128, 35, 35)