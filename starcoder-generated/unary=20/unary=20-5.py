
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v1 = self.deconv(x2)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
