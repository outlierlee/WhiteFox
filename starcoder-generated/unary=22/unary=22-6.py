
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_module = torch.nn.Linear(8, 10)
 
    def forward(self, x1):
        v1 = self.linear_module(x1)
        v2 = torch.tanh(v1)
        return v2

# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(1, 8)
__output2__ = m2(x1)

