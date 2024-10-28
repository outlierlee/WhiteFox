
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)

    def forward(self, x1, x2, inp=None):
        out1 = self.linear(x1)
        out2 = self.linear(x2)
        out3 = torch.mm(out1, out2)
        return out3 + inp

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float)
x2 = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float)
inp = torch.tensor([1, 2, 3], dtype=torch.float)
output = m(x1, x2, inp=inp)

