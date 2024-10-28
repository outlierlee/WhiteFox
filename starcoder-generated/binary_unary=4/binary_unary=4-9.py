
class Model(torch.nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.ln = torch.nn.Linear(d_in, d_out)
 
    def forward(self, x1, other):
        v1 = self.ln(x1)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3

# Initializing the model
d_in, d_out = 16, 8
m = Model(d_in, d_out)

# Inputs to the model
x1 = torch.randn(1, d_in)
other = torch.randn(1, d_out)
