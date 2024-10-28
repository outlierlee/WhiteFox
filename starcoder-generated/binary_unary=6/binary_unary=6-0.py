
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 10)
    
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - 2  # assume other = 2
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(64, 100)
