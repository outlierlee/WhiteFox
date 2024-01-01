
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 1, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 64, 4, padding=0, stride=1)
        self.conv2 = torch.nn.Conv2d(16, 4, 8, padding=0, stride=2)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(64, 16, 2, padding=1, stride=1)
        self.conv3 = torch.nn.Conv2d(4, 4, 2, padding=1, stride=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv_transpose(v2)
        v4 = self.conv2(v3)
        v5 = self.conv_transpose1(v4)
        v6 = torch.relu(v5)
        v7 = self.conv3(v6)
        return v7
# Inputs to the model
x1 = torch.randn(1, 3, 128, 128)