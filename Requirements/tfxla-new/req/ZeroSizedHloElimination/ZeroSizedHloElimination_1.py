import tensorflow as tf

# Create a zero-sized tensor by slicing or reshaping
input_tensor = tf.constant([], shape=(0, 10))  # Zero-sized tensor
output_tensor = tf.reduce_sum(input_tensor)    # Operation on zero-sized tensor
