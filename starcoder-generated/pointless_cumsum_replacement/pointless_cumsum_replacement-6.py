
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, arg1, arg2):
        self.t1 = t1
        self.arg1 = arg1
        self.arg2 = arg2
        t2 = torch.full([arg1, arg2], 1, dtype=t1.dtype, layout=torch.strided, device=t1.device, pin_memory=False)
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model        
m = Model()

# Creating the input tensor
t1s = [(1,2,3), (2,3,4), (4,5,6)] # these should be tuples of 3 numbers
arg1s = [0, 1, 2]
arg2s = [0, 1, 2]

x1 = torch.stack([torch.tensor(tup) for tup in t1s])
y1, y2, y3 = [m(t, a1, a2) for t, a1, a2 in zip(x1, arg1s, arg2s)]

print(y1, y2, y3)
