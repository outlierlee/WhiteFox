
class Model(torch.nn.Module):
    def __init__(self, input_dimension, dropout_p=0.1, scale_factor=0.1):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p
        self.query = torch.nn.Linear(input_dimension, input_dimension)
        self.key = torch.nn.Linear(input_dimension, input_dimension)
        self.value = torch.nn.Linear(input_dimension, input_dimension)
 
    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        v3 = self.value(x2)
        qk = torch.matmul(v1, v2.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, v3)
        return output

# Initializing the model
m = Model(32)

# Inputs to the model
x1 = torch.randn(1, 32)
x2 = torch.randn(1, 32)
