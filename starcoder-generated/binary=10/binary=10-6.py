
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2

# Initializing the model (other tensor is a linear independent variable)
m = Model(torch.randn(10,20))

# Inputs to the model
x1 = torch.randn(10,)
