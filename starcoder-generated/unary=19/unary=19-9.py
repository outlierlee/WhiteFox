
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(64*64*3, 1)
        
    def forward(self, x):
        v1 = self.fc(x)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m2 = Model2()

# Inputs to the model
x = torch.randn(1, 64*64*3)
