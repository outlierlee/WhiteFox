
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(100, 100)
        self.fc1 = torch.nn.Linear(100, 100)
        self.fc2 = torch.nn.Linear(100, 100)
        self.fc3 = torch.nn.Linear(100, 100)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.fc(x1)
        v2 = self.fc1(x2)
        v3 = self.fc2(x3)
        v4 = self.fc3(x4)
        
        v5 = torch.mm(v1, v2)
        v6 = torch.mm(v3, v4)
        v7 = v5 + v6
        
        return v7

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 100)
x2 = torch.randn(1, 100)
x3 = torch.randn(1, 100)
x4 = torch.randn(1, 100)

# Outputs
