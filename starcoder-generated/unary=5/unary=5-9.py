
class Model_2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x2):
        u1 = self.deconv(x2)
        u2 = u1 * 0.5
        u3 = u1 * 0.7071067811865476
        u4 = torch.erf(u3)
        u5 = u4 + 1
        u6 = u2 * u5
        return u6

# Initializing the model
m2 = Model_2()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
