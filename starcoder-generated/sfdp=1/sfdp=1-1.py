
class MyModel(torch.nn.Module):
    def __init__(self, d_input, d_output, d_model, nhead, dropout_p=0.1):
        super().__init__()
        self.qkv = torch.nn.Linear(d_input, d_model * 3)
        self.inv_scale_factor = d_model ** -0.5  
        
    def multi_head_attention(self, query, key, value):
        query, key, value = self.qkv(query, key, value).chunk(3, dim=-1)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m = MyModel(d_input=512, d_output=512, d_model=512, nhead=8)

# Inputs to the model
query = torch.randn(1, 32, 512)
key = torch.randn(1, 32, 512)
value = torch.randn(1, 32, 512)
