
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
att = Attention(dim=128, dropout_p=0.3)

# Inputs to the model
query = torch.randn(1, 16, 128)
key = torch.randn(1, 16, 128)
value = torch.randn(1, 16, 128)
