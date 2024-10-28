
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.unary_op = torch.nn.Tanh()

    def forward(self, x1, x2):
        x3 = torch.cat([x1, x2], dim=-1)
        x4 = x3.view(-1, 7)
        x5 = self.unary_op(x4)
        return x5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 7)
x2 = torch.randn(1, 7)
