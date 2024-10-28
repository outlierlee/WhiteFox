t1 = conv_transpose(input_tensor)  # Apply pointwise transposed convolution to the input tensor
t2 = conv_transpose(input_tensor)  # Apply the same pointwise transposed convolution to the input tensor again
t3 = torch.sigmoid(t2)  # Apply the sigmoid function to the output of the second transposed convolution
t4 = t1 * t3  # Multiply the output of the first transposed convolution by the output of the sigmoid function
