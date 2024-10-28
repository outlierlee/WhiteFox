
class Model(torch.nn.Module):
    def __init__(self, input_shape, num_classes):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(input_shape, num_classes)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2

# Initializing the model
m = Model(64, 10)

# Inputs to the model
x1 = torch.randn(1, 64)
