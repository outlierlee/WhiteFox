t1 = conv_transpose(input_tensor) # Apply a transposed pointwise convolution to the input tensor
t2 = torch.sigmoid(t1) # Apply the sigmoid activation function to the output of the transposed convolution
