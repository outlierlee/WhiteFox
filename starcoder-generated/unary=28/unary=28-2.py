
class Model(torch.nn.Module):
    def __init__(self, min_value=0.0, max_value=1.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 100)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        l1 = F.relu(self.linear(x1))
        l2 = torch.clamp_min(l1, self.min_value)
        l3 = torch.clamp_max(l2, self.max_value)
        return l3

# Initializing the model
m = Model(-1, 1)

# Inputs to the model
x1 = torch.randn(64, 3)
