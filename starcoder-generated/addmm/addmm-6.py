
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model
m2 = Model2()

# Here we are defining its input parameters, x1, x2 and inp.
x1 = torch.randn(64, 64)
x2 = torch.randn(64, 64)
inp = torch.randn(64, 64)

# Passing the arguments to the model
