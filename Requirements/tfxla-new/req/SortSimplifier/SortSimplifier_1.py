# Assume `input_tensor` is a multi-dimensional tensor.
sorted_tuple = tf.sort(input_tensor, axis=-1, direction='ASCENDING', output_type=tf.float32)

# Only use some elements of the sorted tuple.
used_element = tf.gather(sorted_tuple, indices=[0], axis=0)
# Other elements of the tuple are not used in the computation.
