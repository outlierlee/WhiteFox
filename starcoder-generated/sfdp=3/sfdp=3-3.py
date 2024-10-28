
class M(torch.nn.Module):
    def __init__(self, query_dim=8, key_dim=16, value_dim=32, scale_factor=0.2, dropout_p=0.5):
        super().__init__()
        self.query_dim = query_dim
        self.key_dim = key_dim
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        # Multiply query tensor by key tensor
        qk= torch.matmul(query, key.transpose(-2, -1))
        # Scale by factor
        scaled_qk = qk.mul(self.scale_factor)
        # Softmax
        softmax_qk = scaled_qk.softmax(dim=-1)
        # Dropout
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        # Output
        output = torch.matmul(dropout_qk, value)
        return output

# Initializing the model
m = M(8, 16, 32, 0.2, 0.5)

# Inputs to the model
query = torch.randn(64, 8)
key = torch.randn(64, 16)
value = torch.randn(64, 32)
output = m(query, key, value)