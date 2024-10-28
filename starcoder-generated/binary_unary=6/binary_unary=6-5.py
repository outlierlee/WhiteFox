
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(input_size, output_size)

    def forward(self, x):
        r1 = self.linear(x)
        r2 = r1 - 1.0
        r3 = torch.nn.functional.relu(r2)
        return r3

# Initializing the model
m = Model(10, 5)

# Inputs to the model
x = torch.randn(1, 10)
