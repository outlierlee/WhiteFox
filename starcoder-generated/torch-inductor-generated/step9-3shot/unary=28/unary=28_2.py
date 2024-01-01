
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=3)
        v3 = torch.clamp_max(v2, max_value=4)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand(5)