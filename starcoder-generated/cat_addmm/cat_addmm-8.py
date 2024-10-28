
class Model(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.fc1 = torch.nn.Linear(input_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(input_dim, hidden_dim)
 
    def forward(self, x):
        t1 = torch.addmm(x, self.fc1.weight, self.fc2.weight)
        t2 = torch.cat([t1], 1)
        return t2

# Initializing the model
m = Model(100, 10)

# Inputs to the model
x = torch.randn(100)
