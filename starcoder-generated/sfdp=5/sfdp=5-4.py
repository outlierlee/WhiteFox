
class Model(torch.nn.Module):
    def __init__(self, dropout_p):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = self.dropout(attn_weight)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model(0.1)

# Inputs to the model
query = torch.randn(8, 10, 64)
key = torch.randn(8, 10, 64)
value = torch.randn(8, 10, 64)
attn_mask = torch.randn(8, 10, 10)
