
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 128)
        self.fc2 = torch.nn.Linear(128, 128)
 
    def forward(self, x):
        x = self.fc1(x)
        x = x + torch.randn_like(x)
        x = self.fc2(x)
        x = torch.max(x, torch.tensor(0))
        return x

# Initializing the model
model = Model()

# Inputs to the model
x = torch.randn(1, 8)
