import tensorflow as tf

# Assume `some_operation` is an operation that supports BF16 and has F32 output
output = some_operation(input_tensor)

# Convert the output from F32 to BF16
output_bf16 = tf.cast(output, dtype=tf.bfloat16)

# All users of `output` should be using `output_bf16`
result = another_operation(output_bf16)
