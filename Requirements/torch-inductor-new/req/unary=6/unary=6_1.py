t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor again
t3 = t2 + 3  # Add 3 to the output of the second convolution
t4 = torch.clamp_min(t3, 0)  # Clamp the result to have a minimum value of 0
t5 = torch.clamp_max(t4, 6)  # Clamp the result to have a maximum value of 6
t6 = t1 * t5  # Multiply the output of the first convolution by the clamped result
t7 = t6 / 6  # Divide the result by 6
