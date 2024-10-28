
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.unfold = torch.nn.Unfold(kernel_size=3, padding=1)
 
    def forward(self, x1, size):
        v1 = self.unfold(x1)
        v2 = v1[:, :size]
        v3 = torch.cat([v1, v2], dim=1)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn((1, 3, 64, 64))
size = 9223372036854775807
