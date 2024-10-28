t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 > 0 # Compare the output of the convolution to 0
t3 = t1 * negative_slope # Multiply the output of the convolution by a parameter 'negative_slope'
t4 = torch.where(t2, t1, t3) # Use the where function to select between t1 and t3 based on the condition t2
