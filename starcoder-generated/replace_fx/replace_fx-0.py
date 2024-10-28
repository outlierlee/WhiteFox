
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5, True)
        v2 = torch.rand_like(v1, dtype=v1.dtype)
        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
