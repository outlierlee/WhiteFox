
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, value_dim, inv_scale=1):
        super().__init__()
        self.inv_scale = inv_scale
    
    def forward(self, query, key, value):
        scaled_dot_product = torch.bmm(query, key.transpose(1, 2)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = torch.bmm(attention_weights, value)
        return output

# Initializing the model
m = Model(16, 16, 16, 1)

# Inputs to the model
query = torch.randn(1, 1, 16)
key = torch.randn(1, 1, 16)
value = torch.randn(1, 1, 16)
