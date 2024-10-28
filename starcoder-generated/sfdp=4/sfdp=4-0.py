
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(256, 8)
 
    def forward(self, query, key, value, attn_mask):
        output, _ = self.attention(query, key, value, attn_mask=attn_mask)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(10, 16, 256)
key   = torch.randn(10, 16, 256)
value = torch.randn(10, 16, 256)
attn_mask = torch.randn(10, 16, 16)
