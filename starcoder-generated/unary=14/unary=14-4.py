
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = torch.nn.Sigmoid()(v1)
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
