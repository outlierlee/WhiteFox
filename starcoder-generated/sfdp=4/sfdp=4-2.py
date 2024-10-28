
class Model(torch.nn.Module):
    def __init__(self, dim_input):
        super().__init__()
        self.query = torch.nn.Linear(dim_input, dim_input)
        self.key = torch.nn.Linear(dim_input, dim_input)
        self.value = torch.nn.Linear(dim_input, dim_input)
 
    def forward(self, x1, attn_mask):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output

# Initializing the model
m = Model(dim_input=128)

# Inputs to the model
x1 = torch.randn(1, 64, 128)
attn_mask = torch.randn(64, 64) # Some attention mask
