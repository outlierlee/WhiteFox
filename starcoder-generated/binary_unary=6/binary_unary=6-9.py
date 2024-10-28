
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)
 
    def forward(self, x2):
        v1 = self.fc(x2)
        v2 = v1 - 0.3
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 3)
