
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask, dropout_p):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.nn.functional.dropout(attn_weight, dropout_p, training=self.training)
        output = attn_weight @ value
        return output

# Initializing the model and inputs
m = Model()
query = torch.randn(64, 8, 128)
key = torch.randn(64, 8, 128)
value = torch.randn(64, 8, 128)
attn_mask = torch.randn(64, 8, 128)
dropout_p = 0.1

# Compute the output
