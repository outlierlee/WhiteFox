
class ModelLinear(torch.nn.Module):
    def __init__(self):
        super(ModelLinear, self).__init__()
        self.linear_1 = torch.nn.Linear(5, 8)
        self.linear_2 = torch.nn.Linear(8, 16)
        
    def forward(self, x, other):
        x_1 = self.linear_1(x)
        x_2 = x_1 + other
        x_3 = torch.relu(x_2)
        return x_3

# Initializing the model
m_linear = ModelLinear()

# Inputs to the model
x = torch.randn(1, 5)
other = torch.randn(1, 16)
