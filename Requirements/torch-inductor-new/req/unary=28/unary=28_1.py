t1 = linear(input_tensor)  # Apply a pointwise linear transformation to the input tensor
t2 = torch.clamp_min(t1, min_value)  # Clamp the output of the linear transformation to have a minimum value of `min_value`
t3 = torch.clamp_max(t2, max_value)  # Clamp the result to have a maximum value of `max_value`
