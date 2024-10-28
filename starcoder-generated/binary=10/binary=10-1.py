
class LinearAdd(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)
        self.other = torch.randn(output_dim) # Creating a random tensor
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = t1 + self.other
        return t2

# Initializing the model
la = LinearAdd(32, 64)

# Inputs to the model
x = torch.randn(1, 32)
