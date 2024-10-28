
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 4, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = v1 > 0
        v3 = v1 * -0.2
        v4 = torch.where(v2, v1, v1)
        return v4

# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.rand(1, 8, 128, 128)
__output__2 = m2(x2)

