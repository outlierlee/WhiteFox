# Assume lhs and rhs are tensors with shapes that include batch dimensions.
# The batch dimensions are equal and strictly ascending, e.g., [0, 1, 2, ...].
# At least one of these batch dimensions has size 1 in the lhs tensor.

lhs = tf.constant(..., shape=[1, ..., M, K])  # Example shape with a degenerate batch dimension
rhs = tf.constant(..., shape=[1, ..., K, N])  # Corresponding shape for rhs

# Perform a batch dot product with a single contracting dimension.
result = tf.linalg.matmul(lhs, rhs, ...)
