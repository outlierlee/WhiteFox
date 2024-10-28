
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v2 = self.linear(x1)
        v1 = self.sigmoid(v2)
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
