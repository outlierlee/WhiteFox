
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=10.0):
        super(Model, self).__init__()
        self.fc1 = torch.nn.Linear(4, 10)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        x = self.fc1(x)
        x = torch.clamp_min(x, self.min_value)
        x = torch.clamp_max(x, self.max_value)
        return x

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 4)
