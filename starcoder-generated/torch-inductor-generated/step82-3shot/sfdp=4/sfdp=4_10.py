
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, Q, k, v, mask):
        qk = torch.add(Q, mask) @ k.transpose(-2, -1) / math.sqrt(Q.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
# Inputs to the model
Q = torch.randn(1, 64, 56, 56)
K = torch.randn(1, 64, 56, 56)
V = torch.randn(1, 64, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)