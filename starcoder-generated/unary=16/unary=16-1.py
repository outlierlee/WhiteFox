
class LinearReluModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 16)
    
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = torch.nn.functional.relu(v1)
        return v2

# Initializing the model
m = LinearReluModel()

# Inputs to the model
x1 = torch.randn(1, 8)
