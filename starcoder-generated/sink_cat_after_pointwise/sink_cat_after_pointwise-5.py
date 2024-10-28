:
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor1, tensor2):
        v1 = torch.cat([tensor1, tensor2, tensor2], dim=1)
        v2 = v1.view(2, -1)
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
tensor1 = torch.randn(1, 1, 3)
tensor2 = torch.randn(1, 1, 3)
