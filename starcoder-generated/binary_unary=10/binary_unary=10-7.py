
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size, other_size):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, output_size)
        self.other = torch.nn.Parameter(torch.randn(other_size))

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        v3 = F.relu(v2)
        return v3

# Initializing the model
m = Model(128, 64, 64)

# Inputs to the model
x1 = torch.randn(64, 128)
