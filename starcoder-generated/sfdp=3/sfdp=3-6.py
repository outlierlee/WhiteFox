
class Model2(torch.nn.Module):
    def __init__(self, scale_factor: float, dropout_p: float):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m2 = Model2(0.1, 0.2)

# Inputs to the model
batch_size = 64
seq_len = 10
hidden_dim = 256

query = torch.randn(batch_size, seq_len, hidden_dim)
key = torch.randn(batch_size, seq_len, hidden_dim)
value = torch.randn(batch_size, seq_len, hidden_dim)

