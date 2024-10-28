
class Model(torch.nn.Module):
    def __init__(self, hidden_dimension, dropout_p, inv_scale_factor):
        super().__init__()
        self.hidden_dimension = hidden_dimension
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query, key, value):
        conv = torch.matmul(query, key.transpose(-2, -1))
        scaled_conv = conv.div(self.inv_scale_factor)
        softmax_conv = scaled_conv.softmax(dim=-1)
        dropout_conv = torch.nn.functional.dropout(softmax_conv, p=self.dropout_p)
        output = dropout_conv.matmul(value)
        return output

# Initializing the model
m = Model(hidden_dimension=64, dropout_p=0.1, inv_scale_factor=2.0)

# Inputs to the model
q = torch.randn(16, 64)
k = torch.randn(16, 64)
v = torch.randn(16, 64)
