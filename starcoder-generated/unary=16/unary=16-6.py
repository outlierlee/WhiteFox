
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.relu1 = torch.nn.ReLU()
        
    def forward(self, x1):
        t1 = self.linear1(x1)
        t2 = self.relu1(t1)
        
        return t2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.tensor([[0.1, 0.2], [0.3, 0.4]])
