
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = self.relu(t1)
        return t2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 10)
