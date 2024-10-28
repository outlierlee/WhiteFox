t1 = input_tensor.permute(...)  # Permute the input tensor
t2 = torch.nn.functional.linear(t1, ...)  # Apply linear transformation to the permuted tensor
