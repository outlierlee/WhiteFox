t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = conv(input_tensor) # Apply another pointwise convolution with kernel size 1 to the input tensor
t3 = torch.sigmoid(t2) # Apply the sigmoid function to the output of the second convolution
t4 = t1 * t3 # Multiply the output of the first convolution by the sigmoid-transformed output of the second convolution
