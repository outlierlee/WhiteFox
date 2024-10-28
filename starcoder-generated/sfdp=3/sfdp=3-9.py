
class Attention(torch.nn.Module):
    def __init__(self, dim, dropout_p=0.0):
        super().__init__()
        self.dim = dim
        self.scale_factor = 1 / torch.sqrt(torch.tensor(dim, dtype=torch.float))
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, value)
        return output

# Initializing the model
attn = Attention(dim=64, dropout_p=0.2)

# Inputs to the model
query  = torch.randn(1, 32, 64)
key    = torch.randn(1, 32, 64)
value  = torch.randn(1, 32, 64)
