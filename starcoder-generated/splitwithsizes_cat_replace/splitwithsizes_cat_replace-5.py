:
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, split_sizes, dim):
        split_tensors = torch.split(x1, split_sizes, dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        return concatenated_tensor

# Initializing the model
m = Model()

# Inputs to the model
split_sizes = [6, 11, 18, 5]
dim = 1  # dimension along which to split 
x1 = torch.randn(10, 3)
