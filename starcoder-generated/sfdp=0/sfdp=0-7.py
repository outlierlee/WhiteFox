
class Model(torch.nn.Module):
    def __init__(self, d_model, inv_scale):
        super().__init__()
        self.d_model = d_model
        self.inv_scale = inv_scale

    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return output

# Initializing the model
m = Model(64, 8)

# Inputs to the model
x1 = torch.randn(50, 8)  # batch size 50 with d_model 8
x2 = torch.randn(50, 64)
