
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        t1 = self.conv_t(x)
        t2 = self.relu(t1)
        return t2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
