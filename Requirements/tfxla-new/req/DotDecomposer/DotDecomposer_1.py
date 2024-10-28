import tensorflow as tf

# Example tensors
lhs = tf.random.normal([2, 3, 4, 5])  # Shape with batch, non-contracting, and contracting dimensions
rhs = tf.random.normal([2, 5, 6, 7])  # Shape with batch, contracting, and non-contracting dimensions

# Non-canonical dot operation
dot_product = tf.tensordot(lhs, rhs, axes=[[3], [1]])  # Contracting over the last dimension of lhs and second dimension of rhs
