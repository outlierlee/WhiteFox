
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead, dropout):
        super().__init__()
        self.q = torch.nn.Linear(d_model, d_model)
        self.k = torch.nn.Linear(d_model, d_model)
        self.v = torch.nn.Linear(d_model, d_model)
        self.scale = d_model ** -0.5
        self.attn_dropout = torch.nn.Dropout(dropout)
        self.output_linear = torch.nn.Linear(d_model, d_model)
        
    def forward(self, query, key, value, attn_mask=None):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        qk = torch.matmul(q, k.transpose(-2, -1)) * self.scale
        if attn_mask is not None:
            qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = self.attn_dropout(attn_weight)
        output = torch.matmul(attn_weight, v)
        output = self.output_linear(output)
        return output

# Initializing the model
m = Model(128, 8, 0.1)

# Inputs to the model
query = torch.randn(1, 16, 128)
key = torch.randn(1, 16, 128)
value = torch.randn(1, 16, 128)
attn_mask = torch.tril(torch.ones(16, 16))
