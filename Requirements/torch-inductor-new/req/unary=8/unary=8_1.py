t1 = conv_transpose(input_tensor)  # Apply pointwise transposed convolution to the input tensor
t2 = conv_transpose(input_tensor)  # Apply pointwise transposed convolution to the input tensor again
t3 = t2 + 3  # Add 3 to the output of the second transposed convolution
t4 = torch.clamp_min(t3, 0)  # Clamp the result to have a minimum value of 0
t5 = torch.clamp_max(t4, 6)  # Clamp the result to have a maximum value of 6
t6 = t1 * t5  # Multiply the output of the first transposed convolution by the clamped result
t7 = t6 / 6  # Divide the result by 6
