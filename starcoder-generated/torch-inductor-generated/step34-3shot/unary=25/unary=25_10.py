
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(64, 16)
 
    def forward(self, x2):
        v1 = self.linear_1(x2)
        v2 = (v1 > 0)
        v3 = v1 * 0.1
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 64)