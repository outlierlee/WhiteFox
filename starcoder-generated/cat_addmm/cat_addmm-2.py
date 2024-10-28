
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(100, 50)
        self.fc2 = torch.nn.Linear(50, 20)

    def forward(self, input):
        v1 = self.fc1(input)
        output1 = torch.addmm(v1, self.fc2.weight, self.fc2.bias)
        out = torch.cat([output1, v1], dim=0)
        return out
        
# Initializing the model
m = Model()

# Inputs to the model
input = torch.randn(1, 100)
dim = 0
