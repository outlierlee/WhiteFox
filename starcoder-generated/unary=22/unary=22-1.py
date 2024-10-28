
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)
    
    def forward(self, x):
        y1 = self.linear(x)
        y2 = torch.tanh(y1)
        return y2

# Initializing the model  
m = MyModel()

# Inputs to the model
x = torch.randn(64)

output = m(x)