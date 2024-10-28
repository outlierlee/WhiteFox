
class Model(torch.nn.Module):
    def __init__(self, in_features, out_features, bias=True):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features, bias=bias)

    def forward(self, x):
        t1 = self.linear.weight @ x + self.linear.bias
        t2 = torch.cat([t1], 0)
        return t2

# Initializing the model
m = Model(3, 8, bias=True)

# Inputs to the model
x = torch.tensor([1.0, 1.0, 1.0]).unsqueeze(0)
