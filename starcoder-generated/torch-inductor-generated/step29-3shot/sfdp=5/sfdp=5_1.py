
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.heads = 11
        self.seq_len = 99
        self.dim = 20 // self.heads
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = attn_weight @ value
        return output
# Inputs to the model
query = torch.randn(1, 11, 99, 40)
key = torch.randn(1, 11, 99, 40)
value = torch.randn(1, 11, 99, 40)
attn_mask = torch.randn(1, 1, 99, 99)