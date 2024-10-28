
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, x2, size):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, :size]
        v3 = torch.cat([v1, v2], dim=1)
        return v3

# Inputs to the model
x1 = torch.randn(100, 10)
x2 = torch.randn(100, 5)
size = 7
