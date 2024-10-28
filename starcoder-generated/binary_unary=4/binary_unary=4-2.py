
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(100, 200)
        self.linear2 = torch.nn.Linear(200, 200)
 
    def forward(self, x1, other):
        t1 = self.linear1(x1)
        t2 = t1 + other
        t3 = torch.nn.functional.relu(t2)
        return t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(100)
other = torch.randn(200)
