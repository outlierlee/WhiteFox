
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - torch.tensor([2], dtype=torch.float).view(1,1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.tensor([[1.0], [1.0], [2.0]], dtype=torch.float)
