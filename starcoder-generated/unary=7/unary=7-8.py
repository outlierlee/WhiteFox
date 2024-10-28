
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.nn.functional.relu(v1 + 3)
        v3 = v1 * v2
        v4 = v3 / 6
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10)
