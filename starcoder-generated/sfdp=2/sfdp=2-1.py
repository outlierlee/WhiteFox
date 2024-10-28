
class MyModel(torch.nn.Module):
    def __init__(self, d_input, d_output, d_model, nhead, dropout_p=0.1):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, 2 * d_model)
        self.inv_scale_factor = d_model ** -0.5  
        
    def multi_head_attention(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

    def forward(self, query, key, value):
        query = self.qkv(query)
        key = self.qkv(key)
        value = self.qkv(value)
        return self.multi_head_attention(query, key, value, self.inv_scale_factor, dropout_p)

# Initializing the model
m = MyModel(256, 256, 512, 8)

# Inputs to the model
query, key, value = torch.randn(1, 256, 512), torch.randn(1, 256, 512), torch.randn(1, 256, 512)
