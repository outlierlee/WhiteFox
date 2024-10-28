
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(7, 5)
        self.linear2 = torch.nn.Linear(5, 3)

    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = self.linear2(x2)
        summed = torch.addmm(x1, v1, v2)
        cat = torch.cat([summed], 1)
        return cat

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 7)
x2 = torch.randn(10, 5)
