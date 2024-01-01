
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_27 = torch.nn.ConvTranspose2d(27, 27, 4, stride=2, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose_27(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
# Inputs to the model
x1 = torch.randn(1, 27, 150, 150)