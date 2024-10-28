import tensorflow as tf

# Example tensor
input_tensor = tf.random.uniform(shape=[100, 200, 300])

# Reduction operation with dimensions larger than reduce_window_size
# Assume reduce_window_size is less than 100, 200, or 300
reduced_tensor = tf.reduce_sum(input_tensor, axis=[0, 1])
