
class Attention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.embed_dim = embed_dim

    def forward(self, query, key, value, attn_mask=None):
        attn_weight = torch.bmm(query, key.transpose(-2, -1))
        attn_weight = attn_weight / math.sqrt(self.embed_dim)
        if attn_mask is not None:
            attn_weight = attn_weight + attn_mask    
        attn_weight = torch.softmax(attn_weight, dim=-1)
        output = torch.bmm(attn_weight, value)
        return output

# Initializing the model
m = Attention(embed_dim=64)

# Inputs to the model
query = torch.randn(1, 16, 64)
key = torch.randn(1, 16, 64)
value = torch.randn(1, 16, 64)
attn_mask = torch.randn(1, 16)
