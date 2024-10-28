
class ModelAttention(torch.nn.Module):
    def __init__(self, dropout_p, attn_mask):
        super().__init__()
        self.value = torch.nn.Linear(8, 8)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.attn_mask = attn_mask

    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        qk = qk + self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = self.dropout(attn_weight)
        output = torch.matmul(attn_weight, self.value)
        return output

# Initializing the model
m = ModelAttention(0.5, torch.tensor([1., 2., 1., 0.]))

# Inputs to the model
query = torch.tensor([[1.0, 2.0, 3.0, 4.0],
                      [5.0, 6.0, 7.0, 8.0]])
key = torch.tensor([[2.0, 3.0, 4.0, 5.0],
                    [6.0, 7.0, 8.0, 1.0]])
