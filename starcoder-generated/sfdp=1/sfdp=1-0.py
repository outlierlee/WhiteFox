
class Model(torch.nn.Module):
    def __init__(self, hidden_size, dropout_p):
        super(Model, self).__init__()
        self.inv_scale_factor = torch.tensor([math.sqrt(hidden_size)])
        self.dropout_p = dropout_p
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1)
        scaled_qk = qk / self.inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk @ value
        return output

# Initializing the model
m = Model(hidden_size=256, dropout_p=0.1)

# Inputs to the model
query = torch.randn(8, 256)
key = torch.randn(8, 256)
value = torch.randn(8, 256)
