
class Model(torch.nn.Module):
    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, self.dropout_p, True)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model(0.1)

# Inputs to the model
query = torch.randn(1, 8, 512)
key = torch.randn(1, 8, 64)
value = torch.randn(1, 8, 64)
attn_mask = torch.randn(1, 512, 64)
