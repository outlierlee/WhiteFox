
class Model(torch.nn.Module):
    def __init__(self, split_sizes:list, dim: int):
        super().__init__()
        self.split_sizes = split_sizes
        self.dim = dim

    def forward(self, x1):
        v1 = torch.split(x1, self.split_sizes, self.dim)
        v2 = torch.cat(v1, self.dim)
        return v2

    def is_valid_splitwithsizes_cat(self) -> bool:
        return len(torch.split(x1, self.split_sizes, self.dim)) == 1 and torch.cat(torch.split(x1, self.split_sizes, self.dim), self.dim).all()

# Initializing the model
m = Model([2,3,1], 2)

# Inputs to the model
x1 = torch.randn(16, 16, 8, 8)
