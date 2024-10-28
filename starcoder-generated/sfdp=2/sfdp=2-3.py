
class M(torch.nn.Module):
    def __init__(self, query_dim=8, key_dim=16, value_dim=32, inv_scale_factor=2.0, dropout_p=0.1):
        super().__init__()
        self.query_dim = query_dim
        self.key_dim = key_dim
        self.value_dim = value_dim
        self.inv_scale_factor = inv_scale_factor
        self.dropout_p = dropout_p
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(self.inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = self.softmax(scaled_qk) # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, value) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = M()

# Inputs to the model
query = torch.randn(1, 8, 8)
key = torch.randn(1, 8, 16)
value = torch.randn(1, 16, 32)
