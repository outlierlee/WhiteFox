
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = x.view(x.shape[0], -1)
        y = y.tanh()
        x = y.view(x.shape[0], 4)
        y = torch.cat((x, x), dim=0)
        return y.view(x.shape[0] * y.shape[0], -1).tanh()
# Inputs to the model
x = torch.randn(2, 2, 2)