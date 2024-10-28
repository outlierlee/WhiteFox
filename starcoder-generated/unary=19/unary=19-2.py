
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64 * 64, 128)
        self.fc2 = torch.nn.Linear(128, 256)
        self.fc3 = torch.nn.Linear(256, 1)
 
    def forward(self, x1):
        v1 = x1.view(x1.size(0), -1)
        v2 = torch.relu(self.fc1(v1))
        v3 = torch.relu(self.fc2(v2))
        v4 = torch.sigmoid(self.fc3(v3))
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 64)
