
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10, 5)
        self.other = torch.tensor([i*0.2 for i in range(10)])

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 - self.other
        v3 = v2.relu()
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
