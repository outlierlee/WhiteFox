
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1.view(x1.size(0), -1))
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m = Model(-0.01)

# Inputs to the model
x1 = torch.randn(1, 64)
