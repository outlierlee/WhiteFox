 (functional API)
conv = torch.nn.Conv1d(1, 2, kernel_size=1)
bn = torch.nn.BatchNorm1d(2)

def model(x):
    x = torch.nn.functional.conv1d(x, conv.weight, conv.bias)
    x = torch.nn.functional.batch_norm(x, bn.running_mean, bn.running_var, bn.weight, bn.bias, training=False)
    return x

# Input tensor
x = torch.randn(1, 1, 2)
