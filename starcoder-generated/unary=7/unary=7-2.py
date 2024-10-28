
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 128)
        self.fc2 = torch.nn.Linear(128, 10)
 
    def forward(self, x):
        x1 = self.fc1(x)
        x2 = self.fc2(x1)
        x3 = torch.clamp(x2, min=0, max=6)
        x4 = x1 * (x3 + 3)
        x5 = x4 / 6
        return x5

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 8)
