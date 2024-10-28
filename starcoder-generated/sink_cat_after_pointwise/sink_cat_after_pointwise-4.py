
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1, x2):
        all_inputs = torch.cat([x1, x2], dim=1)
        reshaped = all_inputs.view(-1, self.linear.in_features)
        all_inputs_processed = torch.relu(reshaped)
        return self.linear(all_inputs_processed)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 1)
x2 = torch.randn(1, 1, 1)
