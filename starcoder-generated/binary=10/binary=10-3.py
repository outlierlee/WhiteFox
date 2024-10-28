
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=2, out_features=2)
        self.other = other
        
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2

# Initializing the model
other = torch.tensor([[1.0, 1.0]])
m = Model(other)

# Inputs to the model
x1 = torch.randn(1, 2)
x1 = x1.view(1, -1) # explicitly reshaping the input tensor to avoid any errors in the forward method.
