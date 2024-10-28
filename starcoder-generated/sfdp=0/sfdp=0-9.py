
class Model(torch.nn.Module):
    def __init__(self, d_query, d_key):
        super(Model, self).__init__()
        self.inv_scale = d_key ** 0.5
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = torch.matmul(attention_weights, value)
        return output

# Initializing the model
d_query = 32
d_key = 64
m = Model(d_query, d_key)

# Inputs to the model
query = torch.randn(4, 10, d_query)
key = torch.randn(4, 10, d_query)
value = torch.randn(4, 10, d_key)
