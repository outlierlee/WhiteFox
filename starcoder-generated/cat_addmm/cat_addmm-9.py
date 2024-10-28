
class Model(torch.nn.Module):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__()
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
 
    def forward(self, input, mat1, mat2):
        v1 = torch.addmm(input, mat1, mat2)
        v2 = torch.cat([v1, v1, v1], 1)
        return v2

# Initializing the model
m = Model(3, 3, 8, 2, 16)

# Inputs to the model
input = torch.randn(1, 3)
mat1 = torch.randn(3, 8)
mat2 = torch.randn(8, 16)
