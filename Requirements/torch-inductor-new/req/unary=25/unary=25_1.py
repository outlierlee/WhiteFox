# Apply pointwise linear transformation to the input tensor
t1 = linear(input_tensor)

# Check where the output of the linear transformation is greater than 0
mask = t1 > 0

# Apply the PReLU activation function
# If the condition is true (t1 > 0), use t1
# If the condition is false (t1 <= 0), use t1 * negative_slope
output = torch.where(mask, t1, t1 * negative_slope)
