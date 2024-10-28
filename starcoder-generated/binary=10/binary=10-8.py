
class ModelLinear(torch.nn.Module):
    def __init__(self):
        super(ModelLinear, self).__init__()
        self.linear_module = torch.nn.Linear(5, 10)

    def forward(self, x, other):
        v1 = self.linear_module(x)
        v2 = v1 + other
        return v2

# Initializing the model     
m_addition = ModelLinear()

# Inputs to the model
x = torch.randn(1, 5)
other = torch.randn(1, 10)
