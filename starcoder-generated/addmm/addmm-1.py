
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
    
    def forward(self, inp):
        x1 = torch.randn(10, 10)
        x2 = torch.randn(10, 10)  
        
        t1 = torch.mm(x1, x2)
        t2 = t1 + inp
        return t2
      
# Initializing the model
m = MyModel()

# Inputs to the model
inp_tensor = torch.randn(10, 10)
