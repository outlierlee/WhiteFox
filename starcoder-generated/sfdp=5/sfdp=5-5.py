
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, value_dim, dropout_p):
        super().__init__()
        self.attn_scale = math.sqrt(query_dim)
        self.dropout_p = dropout_p

    def forward(self, query, key, value, attn_mask=None):
        v1 = query.matmul(key.transpose(-2, -1)) / self.attn_scale
        if attn_mask is not None:
            v1 = v1 + attn_mask
        v2 = torch.nn.functional.softmax(v1, dim=-1)
        v3 = torch.nn.functional.dropout(v2, p=self.dropout_p, training=self.training)
        output = v3.matmul(value)
        return output

# Initializing the model
m = Model(8, 8, 8, 0.1)

# Inputs to the model  
q = torch.randn(8, 8)
k = torch.randn(8, 8)
v = torch.randn(8, 8)
mask = torch.tril(torch.ones(8, 8)).view(1, 1, 8, 8)
