
class Model(torch.nn.Module):
    def __init__(self, in_features, out_features, bias=True, min_value=-1.5, max_value=1.5):
        super().__init__()
        self.fc = torch.nn.Linear(in_features, out_features, bias)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        x2 = self.fc(x1)
        x3 = torch.clamp_min(x2, self.min_value)
        x4 = torch.clamp_max(x3, self.max_value)
        return x4

# Initializing the model
m = Model(256, 512)

# Inputs to the model
x1 = torch.randn(1, 256)
