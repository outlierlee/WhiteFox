
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(1, 1, 2, bias=False)
        self.bn = torch.nn.BatchNorm1d(1, track_running_stats=True)

    def forward(self, x):
        v1 = torch.nn.functional.conv1d(x, self.conv.weight)
        out = torch.nn.functional.batch_norm(v1, self.bn.running_mean, self.bn.running_var, self.bn.weight, self.bn.bias, training=False)
        return out

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 2)
