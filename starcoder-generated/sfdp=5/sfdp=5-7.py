
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_head, dropout_p):
        super().__init__()
        self.query = torch.nn.Linear(embed_dim, embed_dim)
        self.key = torch.nn.Linear(embed_dim, embed_dim)
        self.value = torch.nn.Linear(embed_dim, embed_dim)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.num_head = num_head
        self.embed_dim = embed_dim

    def forward(self, x1, mask):
        q = self.query(x1).view(-1, self.num_head, self.embed_dim // self.num_head, x1.size(1))
        k = self.key(x1).view(-1, self.num_head, self.embed_dim // self.num_head, x1.size(1))
        v = self.value(x1).view(-1, self.num_head, self.embed_dim // self.num_head, x1.size(1))

        qk = torch.bmm(q.transpose(-2, -1), k) / math.sqrt(x1.size(1))
        qk += mask
        attn_weight = torch.softmax(qk, -1)
        attn_weight = self.dropout(attn_weight)
        output = torch.bmm(attn_weight, v)
        return output

# Initializing the model
model = Model(embed_dim = 512, num_head = 8, dropout_p=0.1)

# Inputs to the model
x1 = torch.randn(1, 15, 512)
mask = torch.randn(1, 15, 15)
