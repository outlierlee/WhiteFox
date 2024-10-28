
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6

# Generating a different model instance and inputs.
print("Model 2")
m2 = Model()
x2 = torch.randn(1, 3, 64, 64)
__output2__ = m2(x2)
```
Please also note that every new model should have different input data, or else it won't reflect real-life differences. The code above generates the second model with different input data than the first one.