import tensorflow as tf

# Assume input_tensor is a larger tensor
input_tensor = tf.constant([...], dtype=tf.float32)

# Slices from the same indices
slice1 = tf.slice(input_tensor, [start1], [size1])
slice2 = tf.slice(input_tensor, [start2], [size2])

# Elementwise operations on slices
result1 = tf.add(slice1, slice1)
result2 = tf.add(slice2, slice2)

# The slices and operations meet the conditions for SliceSinker
