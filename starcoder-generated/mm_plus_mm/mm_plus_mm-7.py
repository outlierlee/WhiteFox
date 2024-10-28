
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4, 8)
        self.linear2 = torch.nn.Linear(8, 4)
        self.linear3 = torch.nn.Linear(8, 4)
        self.linear4 = torch.nn.Linear(4, 8)

    def forward(self, x1, x2, x3, x4):
        v1 = self.linear1(x1)
        v2 = self.linear2(x2)
        v3 = self.linear3(x3)
        v4 = self.linear4(x4)
        v5 = torch.mm(v1, v2)
        v6 = torch.mm(v3, v4)
        output = v5 + v6
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 4)
x2 = torch.randn(32, 8)
x3 = torch.randn(32, 4)
x4 = torch.randn(32, 8)
