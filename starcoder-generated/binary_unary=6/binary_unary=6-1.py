
class Model(torch.nn.Module):
    def __init__(self, input_size, other_size):
        super().__init__()
        self.fc = torch.nn.Linear(input_size, 1)
        self.other = torch.nn.Parameter(torch.rand(other_size))
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 - self.other.expand(v1.size(0), -1)
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model(10, 3) 

# Inputs to the model
x1 = torch.randn(1, 10)
