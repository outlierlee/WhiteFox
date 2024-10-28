
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, value_dim):
        super().__init__()
        self.query = torch.nn.Linear(query_dim, key_dim)
        self.key = torch.nn.Linear(key_dim, key_dim)
        self.value = torch.nn.Linear(value_dim, value_dim)
 
    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        inv_scale = math.sqrt(x2.size(-1))
        scaled_dot_product = torch.matmul(v1, v2.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        v4 = self.value(x2)
        output = attention_weights.matmul(v4)
        return output

# Initializing the model
m = Model(256, 256, 256)

# Inputs to the model
x1 = torch.randn(1, 256)
x2 = torch.randn(1, 256)
