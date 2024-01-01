
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.linear = torch.nn.Linear(100, 100)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3) # for i, value in enumerate(v2): v4[i] = v1[i] if value else v3[i]
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1000)