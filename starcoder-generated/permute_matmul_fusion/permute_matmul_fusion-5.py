
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2)
        v3 = torch.bmm(x1, self.linear.weight.unsqueeze(0))
        v4 = torch.bmm(self.linear.weight.unsqueeze(0), x2)
        return (v2, v3, v4)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 4)
x2 = torch.randn(1, 4, 4)
