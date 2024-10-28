
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.size = 9223372036854775807
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, :self.size]
        v3 = v2[:, :self.size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 512)
x2 = torch.randn(3, 512)
x3 = torch.randn(3, 512)
x4 = torch.randn(3, 512)
