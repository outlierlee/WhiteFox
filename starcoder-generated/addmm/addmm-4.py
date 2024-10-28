
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1: torch.Tensor, x2: torch.Tensor, inp: torch.Tensor) -> torch.Tensor:
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(128, 128)
x2 = torch.randn(128, 128)
inp = torch.randn(128, 128)

