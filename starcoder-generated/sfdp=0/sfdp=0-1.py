
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model

    def forward(self, query, key, value):
        inv_scale = self.d_model ** 0.5
        dot_product = torch.matmul(query, key.transpose(-2, -1))
        scaled_dot_product = dot_product / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = torch.matmul(attention_weights, value)
        return output

# Initializing the model
m = Model(d_model=128)

# Inputs to the model
key = torch.randn(1, 10, 128)
query = torch.randn(1, 10, 128)
value = torch.randn(1, 10, 128)
