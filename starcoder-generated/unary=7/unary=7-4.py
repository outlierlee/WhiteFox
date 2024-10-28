
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = torch.clamp(v1+3, min=0, max=6)
        v3 = v1 * v2
        v4 = v3 / 6
        return v4
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 8)
