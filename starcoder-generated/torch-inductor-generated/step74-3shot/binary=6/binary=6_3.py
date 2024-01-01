
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 10, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.1
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 64)