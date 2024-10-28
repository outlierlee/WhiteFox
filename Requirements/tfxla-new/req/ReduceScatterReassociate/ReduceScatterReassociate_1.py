# Assume rs0 and rs1 are ReduceScatter operations
# that are compatible with each other.
rs0 = tf.reduce_scatter(input_tensor_0, ...)
rs1 = tf.reduce_scatter(input_tensor_1, ...)

# A reduction operation that takes the outputs of rs0 and rs1.
output = reduction_op(rs0, rs1)
