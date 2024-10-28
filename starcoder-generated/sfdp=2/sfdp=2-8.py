
class Model(torch.nn.Module):
    def __init__(self, hidden_dimension):
        super().__init__()
        self.hidden_dimension = hidden_dimension

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(1 / self.hidden_dimension ** 0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m = Model(100)

# Inputs to the model
query = torch.randn(1, 4, 100)
key = torch.randn(1, 4, 100)
value = torch.randn(1, 4, 100)
