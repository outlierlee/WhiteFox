
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1):
        split_sizes = [3, 3, 4]
        split_tensors = torch.split(x1, split_sizes, dim=2)
        output = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=2)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1,10)
