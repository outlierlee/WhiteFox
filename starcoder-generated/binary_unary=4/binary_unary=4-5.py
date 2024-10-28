
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1, other):
        t1 = self.linear(x1)
        t2 = t1 + other
        t3 = self.relu(t2)
        return t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
other = torch.randn(1, 10)
