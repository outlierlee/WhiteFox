
class Attention(torch.nn.Module):
    def __init__(self):
        super(Attention, self).__init__()
        # Initialize the weights of the linear layers as identity matrix
        identity = torch.eye(8)
        self.linear_layers = torch.nn.ModuleList([torch.nn.Linear(8, 8, bias=False) for _ in range(2)])
        for l in self.linear_layers:
            l.weight.data = identity
        self.scale = 1 / (8 ** 0.5)

    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = torch.matmul(attention_weights, value)
        return output

# Initializing the model
m = Attention()

# Inputs to the model
query = torch.randn(2, 8)
key = torch.randn(2, 8)
value = torch.randn(2, 8)
