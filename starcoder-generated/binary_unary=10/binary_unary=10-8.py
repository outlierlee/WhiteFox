
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10, 5)
        self.act = torch.nn.ReLU()
 
    def forward(self, x):
        t1 = self.fc(x)
        t2 = t1 + torch.ones(x.size())
        t3 = self.act(t2)
        return t3

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(10)
