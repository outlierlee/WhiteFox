
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
model = Model()

# Inputs to the model
query = torch.randn(1, 32, 4)
key = torch.randn(1, 32, 4)
value = torch.randn(1, 32, 4)
inv_scale_factor = 1.0 / 9801
dropout_p = 0.1

# Outputs from the model
output = model(query, key, value, inv_scale_factor, dropout_p)