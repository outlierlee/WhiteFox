
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)
 
    def forward(self, x1, x2):
        v1 = self.fc(x1)
        v2 = v1 + x2
        v3 = torch.maximum(v2, torch.tensor(0.0))
        return v3

# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(1, 3)
x2 = torch.randn(1, 8)
