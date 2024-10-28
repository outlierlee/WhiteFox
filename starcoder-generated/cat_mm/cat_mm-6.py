
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, d):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1 for _ in range(d)], 0)
        return v2

# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(3, 3)
x2 = torch.randn(3, 3)
concat_count = 5
