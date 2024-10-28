
class Model(torch.nn.Module):
    def __init__(self, p=0.5, inplace=False):
        super().__init__()
        self.dropout = torch.nn.Dropout(p, inplace)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5, False)
        v2 = torch.rand_like(x1)
        return v1 + v2

# Initializing the model
m = Model()

# Input for the model
x1 = torch.randn(2, 2)
