
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)
    
    def forward(self, x):
        y = self.linear(x)
        y -= 1.0
        return y

# Initializing the model
m = MyModel()

# Inputs to the model
x1 = torch.randn(16, 64)
