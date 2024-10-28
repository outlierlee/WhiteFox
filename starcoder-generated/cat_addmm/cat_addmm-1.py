
class MyModule(torch.nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()

    def forward(self, x):
        mat1 = torch.randn(64, 64)
        mat2 = torch.randn(64, 64)
        t1 = torch.addmm(x, mat1, mat2)
        t2 = torch.cat([t1], 0)
        return t2

# Initializing model
module = MyModule()

# input tensor
x = torch.randn(1, 64, 64)
