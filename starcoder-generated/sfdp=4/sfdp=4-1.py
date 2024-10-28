
class MyTransformer(torch.nn.Module):
    def __init__(self, d_model, nhead):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_model, nhead)
 
    def forward(self, query, key, value):
        scale = query.size(-1)**-0.5
        qk = query @ (key.transpose(-2,-1) * scale)
        attn_output, attn_output_weights = self.attn(query, key, value)
        return attn_output

# Initializing the model
trans = MyTransformer(4, 2)

# Inputs to the model
query = torch.randn(10, 30, 4)
key = torch.randn(10, 30, 4)
value = torch.randn(10, 30, 4)
