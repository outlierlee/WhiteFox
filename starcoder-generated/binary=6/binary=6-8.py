
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.fc(x1)
        other = 2 * torch.ones_like(v1)  # other is a twice of ones with the same shape as v1
        v2 = v1 - other
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
