
class M(torch.nn.Module):
    def __init__(self, query_dim=8, key_dim=16, value_dim=32, inv_scale_factor=2, dropout_p=0.5):
        super().__init__()
        self.query_dim = query_dim
        self.key_dim = key_dim
        self.value_dim = value_dim
        self.inv_scale_factor = inv_scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m = M()

# Inputs to the model
query = torch.randn(1, 8, 64)
key = torch.randn(1, 16, 64)
value = torch.randn(1, 32, 64)
