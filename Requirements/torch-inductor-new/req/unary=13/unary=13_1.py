t1 = linear(input_tensor) # Apply a pointwise linear transformation to the input tensor
t2 = linear(input_tensor) # Apply the same pointwise linear transformation to the input tensor
t3 = torch.sigmoid(t2) # Apply the sigmoid activation function to the output of the linear transformation
t4 = t1 * t3 # Element-wise multiply the output of the first linear transformation by the sigmoid-activated output of the second linear transformation
