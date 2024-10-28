
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 128)
        self.fc2 = torch.nn.Linear(128, 128)
        self.fc3 = torch.nn.Linear(128, 1)

    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
        v4 = self.fc2(v3)
        v5 = v4 - other
        v6 = torch.relu(v5)
        v7 = self.fc3(v6)
        return v7

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
other = torch.tensor([2.0]) 

