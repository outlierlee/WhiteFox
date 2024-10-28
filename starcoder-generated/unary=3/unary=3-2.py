
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 32, 5, stride=1, padding=2)
        self.conv4 = torch.nn.Conv2d(32, 64, 7, stride=1, padding=3)
        self.conv5 = torch.nn.Conv2d(64, 128, 9, stride=1, padding=4)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = v5 * 0.5
        v7 = v5 * 0.7071067811865476
        v8 = torch.erf(v7)
        v9 = v8 + 1
        v10 = v6 * v9
        return v10

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
