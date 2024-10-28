t1 = conv_transpose(input_tensor)  # Apply pointwise transposed convolution to the input tensor
t2 = t1 > 0  # Compare the output of the transposed convolution with 0
t3 = t1 * negative_slope  # Multiply the output of the transposed convolution by a negative slope
t4 = torch.where(t2, t1, t3)  # Use the where function to select between t1 and t3 based on the condition t2
