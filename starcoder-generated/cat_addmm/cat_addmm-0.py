
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2, 1)
        self.fc2 = torch.nn.Linear(2, 1)

    def forward(self, x):
        t1 = torch.addmm(x, self.fc1.weight, self.fc2.weight)
        t2 = torch.cat([t1], 0)
        return t2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2)
