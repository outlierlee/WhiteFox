# Apply pointwise transposed convolution to the input tensor
t1 = conv_transpose(input_tensor)

# Multiply the output of the transposed convolution by 0.5
t2 = t1 * 0.5

# Apply pointwise transposed convolution to the input tensor
t3 = conv_transpose(input_tensor)

# Apply pointwise transposed convolution to the input tensor
t4 = conv_transpose(input_tensor)

# Apply pointwise transposed convolution to the input tensor
t5 = conv_transpose(input_tensor)

# Multiply the outputs of the transposed convolutions
t6 = t3 * t4 * t5

# Apply pointwise transposed convolution to the input tensor
t7 = conv_transpose(input_tensor)

# Multiply the result by 0.044715
t8 = t6 * 0.044715

# Add the result to the output of another transposed convolution
t9 = t7 + t8

# Multiply the result by 0.7978845608028654
t10 = t9 * 0.7978845608028654

# Apply the hyperbolic tangent function
t11 = torch.tanh(t10)

# Add 1 to the result
t12 = t11 + 1

# Multiply the result by the output of the initial transposed convolution
t13 = t2 * t12
