
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        l1 = self.linear(x1)
        a1 = self.relu(l1)
        return a1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16)
