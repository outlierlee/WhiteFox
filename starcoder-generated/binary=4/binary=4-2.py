
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 128)
        self.fc2 = torch.nn.Linear(128, 10)
 
    def forward(self, x1):
        x2 = self.fc1(x1)
        x3 = torch.nn.functional.relu(x2)
        x4 = self.fc2(x3)
        return x4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
