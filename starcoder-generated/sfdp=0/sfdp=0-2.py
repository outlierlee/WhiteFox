
class Model(torch.nn.Module):
    def __init__(self, d_model, inv_scale):
        super().__init__()
        self.d_model = d_model
        self.inv_scale = inv_scale

    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = torch.matmul(attention_weights, value)
        return output

# Initializing the model
d_model = 512
inv_scale = np.sqrt(d_model)
m = Model(d_model, inv_scale)

# Inputs to the model
query = torch.randn(32, 64, d_model)
key = torch.randn(32, 64, d_model)
value = torch.randn(32, 64, d_model)
