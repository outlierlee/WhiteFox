
class Model(torch.nn.Module):
    def __init__(self, dropout_p):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)
        
    def forward(self, query, key, value, attn_mask=None):
        # Compute the dot product of the query and key and scale it
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        # Add the attention mask if provided
        if attn_mask is not None:
            qk = qk + attn_mask
        # Apply softmax and dropout
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = self.dropout(attn_weight)
        # Compute the dot product of the dropout output and the value
        output = attn_weight @ value
        return output

# Initializing the model
m = Model(0.2)

# Inputs to the model
query = torch.randn(1, 10, 64)
key = torch.randn(1, 10, 64)
value = torch.randn(1, 10, 64)
attn_mask = torch.randn(1, 10, 10)
