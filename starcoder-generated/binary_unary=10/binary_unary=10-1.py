
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 128)
        self.linear2 = torch.nn.Linear(128, 64)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.randn(1, 64)
        v3 = v1 + v2
        v4 = self.linear2(v3)
        v5 = torch.nn.functional.relu(v4)
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64)
