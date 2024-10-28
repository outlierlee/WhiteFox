
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 + x2
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

# Some other tensor to add to the output of the convolution. 
# Here, I am using zeros for example.
other = torch.zeros(1, 8, 64, 64)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
