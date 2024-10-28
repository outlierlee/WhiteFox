
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(512, 512)
        self.k = torch.nn.Linear(512, 512)
        self.v = torch.nn.Linear(512, 512)
 
    def forward(self, x1, x2, x3):
        q = self.q(x1)
        k = self.k(x2)
        value = self.v(x3)
        qk = torch.matmul(q, k.transpose(-2, -1))
        qk = qk / 2.8284271247461903 # We are assuming this is the inverse scale factor
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = torch.matmul(dropout_qk, value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 512)
x2 = torch.randn(1, 512)
x3 = torch.randn(1, 512)
