
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 10)
    
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + x
        return v2

# Initializing the model
m = Model()

# Generating the input tensor
x = torch.randn(1, 100)
