
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8 * 64 * 64, 8 * 64 * 64)
        
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.linear(x1.view(x1.size(0), -1))
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Output
