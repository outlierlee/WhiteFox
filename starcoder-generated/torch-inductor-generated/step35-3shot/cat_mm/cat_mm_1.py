
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v = [torch.mm(x1, x2) for _ in range(5)]
        v = [torch.mm(x1, x2) for _ in range(10)] + v
        return torch.cat(v, 1)
# Inputs to the model
x1 = torch.randn(2, 2)
x2 = torch.randn(2, 2)