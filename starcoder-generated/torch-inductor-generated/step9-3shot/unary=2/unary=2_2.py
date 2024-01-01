
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 5, 2, padding=1)
        self.avgpool2d = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=0, ceil_mode=False, count_include_pad=True)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v10 = v9.contiguous()
        v11 = self.avgpool2d(v10)
        return v11
# Inputs to the model
x1 = torch.randn(1, 3, 3, 3)