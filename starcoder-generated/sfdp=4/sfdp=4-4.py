
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(16, 8)
        self.k = torch.nn.Linear(16, 8)
        self.v = torch.nn.Linear(16, 8)
 
    def forward(self, x):
        query = self.q(x)
        key = self.k(x)
        value = self.v(x)
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_mask = torch.ones_like(qk) 
        attn = torch.softmax(qk, dim=-1)
        attn_weight = attn + attn_mask
        output = attn_weight @ value 
        return output

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 16)
