
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 - other # Subtract 'other' from the output of the convolution
        return v2

# Initializing the model
m = Model()

# Inputs to the model. Here other tensor is used as input instead of scalar.
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 8, 64, 64)
