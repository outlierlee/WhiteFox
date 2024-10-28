
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)

    def forward(self, x1, x2, repeat):
        t1 = torch.mm(x1, x2)
        t2 = torch.cat([t1]*repeat)
        return self.linear(t2)

# Initializing the model
my_model = MyModel()

# Inputs to the model
x1 = torch.randn(3, 8)
x2 = torch.randn(8, 16)
repeat = 5
x3 = torch.randn(5, 16)

# The Forward pass
