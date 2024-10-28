
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.unfold = torch.nn.Unfold(kernel_size=3, padding=1)
 
    def forward(self, x1):
        v1 = self.unfold(x1) 
        v2 = torch.split(v1, [17, 17, 17], dim=1) 
        v3 = torch.cat(v2[::-1], dim=1)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
