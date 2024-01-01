
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 3)
    def forward(self, x):
        x = self.layers(x)
        x = x * 3
        x = torch.unsqueeze(x, dim=0)
        x = torch.flip(x, dims=(0, 1))
        x = torch.sum(x, dim=1)
        x = torch.squeeze(x, dim=0)
        x = torch.stack((x, x), dim=1)
        x = torch.flip(x, dims=(1,))
        return x
# Inputs to the model
x = torch.randn(2, 2)