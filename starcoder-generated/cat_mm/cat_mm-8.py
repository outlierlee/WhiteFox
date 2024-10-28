
class Model(torch.nn.Module):
    def __init__(self, len_of_list):
        super().__init__()
        self.len_of_list = len_of_list

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = [v1 for _ in range(self.len_of_list)]
        v3 = torch.cat(v2, dim=1)
        return v3

# Initializing the model
m = Model(3)

# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(4, 5)
