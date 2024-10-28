
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x2, other=0.0):
        v1 = self.linear(x2)
        v2 = v1 - other
        v3 = self.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 8)
