
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.split
        self.cat = torch.cat
    
    def forward(self, x):
        split_tensors = self.split(x, torch.tensor([1, 2, 3]), dim=0)
        res = [split_tensors[i] for i in range(len(split_tensors))]
        cat = self.cat(res, dim=0)
        return cat

# Initializing the model
model = MyModel()

# Input to the model
x = torch.randn(9)
