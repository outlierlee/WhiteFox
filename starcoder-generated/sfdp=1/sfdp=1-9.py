
class Attention(torch.nn.Module):
    def __init__(self, dim, dropout_p=0.0):
        super().__init__()
        self.dim = dim
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(math.sqrt(self.dim))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
attn = Attention(64, dropout_p=0.1)

# Inputs to the model
query = torch.randn(1, 64, 64)
key = torch.randn(1, 64, 64)
value = torch.randn(1, 64, 64)
