l1 = linear(input_tensor) # Apply pointwise linear transformation to the input tensor
l2 = l1 + 3 # Add 3 to the output of the linear transformation
l3 = torch.clamp_min(l2, 0) # Clamp the result to have a minimum value of 0
l4 = torch.clamp_max(l3, 6) # Clamp the result to have a maximum value of 6
l5 = l1 * l4 # Multiply the output of the linear transformation by the clamped result
l6 = l5 / 6 # Divide the result by 6
