
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.ModuleDict({"conv1": torch.nn.Conv2d(3, 32, 3, 1, 1), "conv2": torch.nn.Conv2d(32, 32, 3, 1, 1), "conv3": torch.nn.Conv2d(32, 32, 3, 1, 2)})
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)