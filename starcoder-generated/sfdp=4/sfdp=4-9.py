
class Model(torch.nn.Module):
    def __init__(self, d_model, n_heads, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.query = torch.nn.Linear(d_model, d_model)
        self.key = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)
        self.attn_dropout = torch.nn.Dropout(dropout)
 
    def forward(self, query, key, value):
        query = self.query(query)
        key = self.key(key)
        value = self.value(value)
        qk = query @ key.transpose(-2, -1) / math.sqrt(self.d_model)
        attn_weight = self.attn_dropout(torch.softmax(qk, dim=-1))
        output = attn_weight @ value
        return output

# Initializing the model
m = Model(512, 8)

# Inputs to the model
q = torch.randn(1, 256, 512)
k = torch.randn(1, 256, 512)
v = torch.randn(1, 256, 512)
