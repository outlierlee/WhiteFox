
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.query = torch.nn.Linear(embed_dim, embed_dim)
        self.key = torch.nn.Linear(embed_dim, embed_dim)
        self.value = torch.nn.Linear(embed_dim, embed_dim)
        self.num_heads = num_heads
 
    def forward(self, x, attn_mask):
        batch_size = x.size(0)
        query = self.query(x)
        key = self.key(x)
        value = self.value(x)
        
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value  
        
        return output
        
# Initializing the model
m = Model(512, 8)

# Inputs to the model
x = torch.rand((32, 128, 512))
attn_mask = torch.ones((32, 128, 128))
