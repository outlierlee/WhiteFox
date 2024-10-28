
class Model(torch.nn.Module):
    def __init__(self, embed_dim, dropout_p=0.1):
        super().__init__()
        self.attn_dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x, attn_mask):
        t1, t2 = x.chunk(2, 2)
        qk = torch.bmm(t1, t2.transpose(1, 2)) / math.sqrt(t1.size(-1))  # batch matrix multiplication
        qk = qk + attn_mask
        attn_weight = torch.nn.functional.softmax(qk, dim=-1)  # attention weights
        attn_weight = self.attn_dropout(attn_weight) # dropout
        output = torch.bmm(attn_weight, t2)
        return output

# Initializing the model
m = Model(embed_dim=64)

# Inputs to the model
x = torch.randn(1, 4, 64)
attn_mask = torch.randn(1, 4, 4)

# generate the output
