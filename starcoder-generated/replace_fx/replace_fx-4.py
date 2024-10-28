
# Define a model with a Conv2d operation followed by a Dropout operation
class NewModel(nn.Module):
    def __init__(self):
        super(NewModel, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 5)
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, x):
        x = self.conv1(x)
        x = torch.nn.functional.max_pool2d(self.dropout(x), 2)
        return x

m = NewModel()

# Inputs to the model
x = torch.randn(1, 3, 5, 5)
