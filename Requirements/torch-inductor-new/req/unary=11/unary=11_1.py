t1 = conv_transpose(input_tensor) # Apply pointwise transposed convolution with kernel size 1 to the input tensor
t2 = t1 + 3 # Add 3 to the output of the transposed convolution
t3 = torch.clamp_min(t2, 0) # Clamp the result to have a minimum value of 0
t4 = torch.clamp_max(t3, 6) # Clamp the result to have a maximum value of 6
t5 = t4 / 6 # Divide the clamped result by 6
