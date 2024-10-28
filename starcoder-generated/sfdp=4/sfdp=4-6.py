
class Model(torch.nn.Module):
    def __init__(self, dmodel):
        super().__init__()
        self.key = torch.nn.Linear(dmodel, dmodel)
        self.query = torch.nn.Linear(dmodel, dmodel)
        self.value = torch.nn.Linear(dmodel, dmodel)
 
    def forward(self, x, mask):
        query = self.query(x)
        key = self.key(x)
        value = self.value(x)

        dot_product = query @ key.transpose(-2,-1) 
        scaled_dot_product = dot_product / math.sqrt(query.size(-1))
        masked_scaled_dot_product = scaled_dot_product + mask
        attn_weight = torch.softmax(masked_scaled_dot_product, dim=-1)
        output = attn_weight @ value
        return output

# Initializing the model
dmodel = 64
m = Model(dmodel)

# Inputs to the model
x = torch.randn(1, 3, dmodel)
mask = torch.randn(1, 3, dmodel)
