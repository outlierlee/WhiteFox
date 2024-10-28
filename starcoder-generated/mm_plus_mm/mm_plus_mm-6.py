
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        m1 = torch.mm(x1, x2)
        m2 = torch.mm(x3, x4)
        v3 = m1 + m2
        return v3

# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(10, 10)
x2 = torch.randn(10, 10)
x3 = torch.randn(10, 10)
x4 = torch.randn(10, 10)
