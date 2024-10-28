:
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1]*3)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 256, requires_grad=True)
x2 = torch.randn(256, 128, requires_grad=True)
