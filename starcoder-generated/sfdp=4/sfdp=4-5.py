
class Attention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        self.sqrt_dim = math.sqrt(self.head_dim)

    def forward(self, query, key, value, mask=None):
        batch_size, seq_length, _ = query.size()
        seq_length2 = key.size(1)

        q = self.unify_heads(query)
        k = self.unify_heads(key)
        v = self.unify_heads(value)

        attn_score = torch.bmm(q, k.transpose(1, 2)) / self.sqrt_dim

        if mask is not None:
            attn_score = attn_score.masked_fill(mask == 0, float('-inf'))

        attn_weight = torch.softmax(attn_score, dim=-1)
        output = torch.bmm(attn_weight, v).contiguous().view(batch_size, seq_length, -1)
        return output

    def unify_heads(self, tensor):
        out_dim = tensor.size(1)
        bs = tensor.size(0)
        tensor = tensor.view(bs, out_dim, self.num_heads, -1).transpose(1, 2)
        return tensor.contiguous().view(bs, -1, self.head_dim)

# Initializing the model
attn = Attention(100, 8)

# Inputs to the model
query = torch.randn(4, 10, 100)
key = torch.randn(4, 10, 100)
value = torch.randn(4, 10, 100)
mask = torch.randint(low=0, high=2, size=(4, 10, 10)).bool()
