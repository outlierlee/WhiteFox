# Example pattern in TensorFlow
x = ...  # Some tensor
y = ...  # Another tensor

# AllReduce operations
ar_x = tf.raw_ops.AllReduce(input=x, ...)
ar_y = tf.raw_ops.AllReduce(input=y, ...)

# Binary operation using the results of AllReduce
result = tf.add(ar_x, ar_y)  # This could be any compatible binary operation
