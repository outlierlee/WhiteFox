
class ModelLinearRelu(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)

    def forward(self, x1):
        x2 = self.fc(x1)
        x3 = torch.nn.functional.relu(x2)
        return x3

# Initializing the model
m = ModelLinearRelu()

# Inputs to the model
x1 = torch.randn(1, 3)
