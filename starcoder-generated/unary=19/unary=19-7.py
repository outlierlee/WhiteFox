
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = torch.nn.Linear(input_size, output_size)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model(512, 1)

# Inputs to the model
x1 = torch.randn(1, 512)
