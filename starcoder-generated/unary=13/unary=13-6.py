
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 16)
        self.linear2 = torch.nn.Linear(16, 32)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        out1 = self.linear1(x1)
        out2 = self.sigmoid(out1)
        out3 = out1 * out2
        return self.linear2(out3)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
