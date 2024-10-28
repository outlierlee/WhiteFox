
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_module = torch.nn.Linear(64, 64)
 
    def forward(self, x2):
        v1 = self.linear_module(x2)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6