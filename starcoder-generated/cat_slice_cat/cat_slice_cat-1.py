
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
    
    def forward(self, x):
        y = torch.cat([x, self.linear(x)], dim=1)
        z = y[:, 0:10]
        return torch.cat([y, z], dim=1)

# Initializing the model
m = MyModel()

# Inputs to the model
x = torch.randn(1, 10)
