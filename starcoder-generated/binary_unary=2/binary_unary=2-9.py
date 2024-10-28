
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 8, 1, stride=1, padding=0)
        
    def forward(self, x1, moo_tensor):
        v1 = self.conv(x1)
        v2 = v1 - moo_tensor
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 16, 16)
moo_tensor = torch.tensor([1])
