
class Model(torch.nn.Module):
    def __init__(self, hidden_size, dropout_p):
        super(Model, self).__init__()
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        
    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(self.hidden_size)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, v)
        return output

# Initializing the model
m = Model(hidden_size=512, dropout_p=0.1)

# Inputs to the model
q = torch.randn(1, 50, 512)
k = torch.randn(1, 60, 512)
v = torch.randn(1, 60, 512)
