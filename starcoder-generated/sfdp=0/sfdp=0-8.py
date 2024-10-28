
class ScaledDotProductAttention(torch.nn.Module):
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Initializing the model
sdp_attn = ScaledDotProductAttention()

# Inputs to the model
query = torch.randn(1, 3, 4)
key = torch.randn(1, 4, 3)
value = torch.randn(1, 4, 5)
inv_scale = torch.tensor(4.0)
