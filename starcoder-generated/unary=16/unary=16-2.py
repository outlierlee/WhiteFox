
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        x1 = x1.view(x1.size(0), -1)
        output = self.linear(x1)
        output = self.relu(output)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
