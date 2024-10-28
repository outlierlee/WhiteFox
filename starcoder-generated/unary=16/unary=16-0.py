
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.relu(v1)
        return v2

# Initializing the model
m = Model()

# Generating inputs
x1 = torch.randn(1, 10)
