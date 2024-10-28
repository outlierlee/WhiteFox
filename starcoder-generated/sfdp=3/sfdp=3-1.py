
class MyModel(torch.nn.Module):
    def __init__(self, d_input, d_output, d_model, nhead, dropout_p=0.1):
        super().__init__()
        self.qkv = torch.nn.Linear(d_input, d_model * 3)
        self.output = torch.nn.Linear(d_model, d_output)
        self.scale_factor = d_model ** -0.5
        self.nhead = nhead
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x):
        qkv = self.qkv(x).reshape(-1, x.size(1), self.nhead, 3 * self.d_model // self.nhead)
        query, key, value = qkv.split([self.d_model // self.nhead, self.d_model // self.nhead, self.d_model // self.nhead], dim=3)
        qk = torch.einsum('bthw,bThw->bhtT', query, key)
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=3)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.einsum('bhtT,bThw->bthw', dropout_qk, value)
        return self.output(output)
    
# Initializing the model
m = MyModel(3, 3, 8, 2, dropout_p=0.2)

# Inputs to the model
x = torch.randn(1, 16, 3)
