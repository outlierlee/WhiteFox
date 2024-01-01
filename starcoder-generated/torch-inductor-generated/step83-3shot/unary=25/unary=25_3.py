
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        
        # Define the negative slope
        negative_slope = 0.01
        t2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(t2, v1, v3)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 8)