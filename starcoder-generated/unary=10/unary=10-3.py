
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(in_features=2, out_features=8)
        self.relu6 = torch.nn.ReLU6()

    def forward(self, x1):
        l1 = self.l1(x1)
        l2 = l1 + 3
        l3 = self.relu6(l2)
        l4 = l3 / 6
        return l4

# Initializing the model and input
m2 = Model2()
x1 = torch.randn(1, 2)
