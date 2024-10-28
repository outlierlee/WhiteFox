
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 8, 2, stride=2, padding=0)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.relu(v1)
        return v2

# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
