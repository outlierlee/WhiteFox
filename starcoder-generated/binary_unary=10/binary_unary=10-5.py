
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 8)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = self.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 128)
other = torch.randn(1, 8) # An additional tensor with the same shape as the output of the linear transformation
