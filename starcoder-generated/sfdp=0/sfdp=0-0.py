
class ModelAttention(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model

    def forward(self, query, key, value):
        inv_scale = math.sqrt(self.d_model)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Pseudocode
# Initialize the model
m = ModelAttention(512)

# Define the input data sizes accordingly
query = torch.randn(1, 12, 512)
key = torch.randn(1, 12, 512)
value = torch.randn(1, 12, 512)

# Model forward
