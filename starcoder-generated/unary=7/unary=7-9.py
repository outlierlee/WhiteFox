
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)
 
    def forward(self, x2):
        v2 = self.fc(x2)
        v3 = v2 * torch.clamp(v2 + 3, min=0, max=6)
        v4 = v3 / 6
        return v4

# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 3)
