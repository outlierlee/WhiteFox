
class M(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = v1.view(1, -1)
        v3 = torch.relu(v2)
        return v3

# Initializing the model
model = M()

# Inputs to the model
x1 = torch.tensor([1.0, 2.0, 3.0])
x2 = torch.tensor([4.0, 5.0, 6.0])
