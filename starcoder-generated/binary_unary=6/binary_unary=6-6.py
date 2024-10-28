
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 - 0.12918585403926324 # Use a constant
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
x1 = torch.nn.init.xavier_normal_(x1, gain=1) # Xavier initializer
