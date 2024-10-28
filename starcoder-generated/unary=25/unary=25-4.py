
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.lin(x1).unsqueeze(-1) # Unsqueezing to maintain shape of 2nd dimension
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4.squeeze(-1) # Squeezing to restore shape of 2nd dimension

# Initializing the model
m = Model(-0.1)

# Inputs to the model
x1 = torch.randn(1, 3)
