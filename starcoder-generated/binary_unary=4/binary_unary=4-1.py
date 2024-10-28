
class LinearReluModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 64)
        self.fc2 = torch.nn.Linear(64, 10)
 
    def forward(self, x1, other):
        t1 = self.fc1(x1)
        t2 = t1 + other
        t3 = torch.nn.functional.relu(t2)
        return t3

# Initializing the model with two input tensors
linear_relu_model = LinearReluModel()

#Inputs to the model
input_tensor = torch.randn(1, 32)
other_tensor = torch.randn(1, 32)
