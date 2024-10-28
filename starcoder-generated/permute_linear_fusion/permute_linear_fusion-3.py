
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x2):
        v1 = x2.permute(0, 1, 3, 2)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 2, 2, 2)
__output2__ = m2(x2)