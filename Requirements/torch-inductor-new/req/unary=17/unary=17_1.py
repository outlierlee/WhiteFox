t1 = conv_transpose(input_tensor) # Apply a transposed pointwise convolution to the input tensor
t2 = torch.relu(t1) # Apply the ReLU activation function to the output of the transposed convolution
