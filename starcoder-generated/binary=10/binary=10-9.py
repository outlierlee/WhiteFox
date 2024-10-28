
class Model(torch.nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.ln = torch.nn.Linear(d_in, d_out)
 
    def forward(self, x1, other):
        v1 = self.ln(x1)
        v2 = v1 + other
        return v2

# Initializing the model (assuming d_in=100 and d_out=200)
m = Model(100, 200)

# Inputs to the model
x1 = torch.randn(100)
other = torch.randn(200)
