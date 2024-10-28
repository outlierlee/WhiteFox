
class Model(torch.nn.Module):
    def __init__(self, dim, inv_scale):
        super().__init__()
        self.dim = dim
        self.inv_scale = inv_scale

    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = torch.matmul(attention_weights, value)
        return output 

# Initializing the model
m = Model(dim=32, inv_scale=math.sqrt(32))

# Inputs to the model
query = torch.randn(1, 32)
key = torch.randn(1, 32)
value = torch.randn(1, 32)
