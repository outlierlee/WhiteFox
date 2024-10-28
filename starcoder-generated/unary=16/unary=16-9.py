
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 10)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.relu(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 30)
