
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(input_size, output_size)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 > 0
        v3 = v1 * -0.01
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model
model = Model(5, 6)

# Inputs to the model
x = torch.ones(2, 5)  # Input tensor
