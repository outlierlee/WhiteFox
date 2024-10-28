
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.series_separation = torch.nn.Linear(2, 1)

    def forward(self, input1, input2):
        concated = torch.cat([input1, input2], dim=1)
        flattened = concated.view(concated.shape[0], -1)
        activated = torch.nn.functional.relu(flattened)
        return torch.nn.functional.linear(activated, self.series_separation.weight, self.series_separation.bias)

# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(1,2)
input2 = torch.randn(1,2)
