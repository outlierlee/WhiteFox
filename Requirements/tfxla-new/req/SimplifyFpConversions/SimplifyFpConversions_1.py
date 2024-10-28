# Assume `input_tensor` is a tensor with a floating-point data type.
t1 = tf.cast(input_tensor, dtype=tf.float32)
t2 = tf.cast(t1, dtype=tf.float64)
t3 = tf.cast(t2, dtype=tf.float16)
t4 = tf.cast(t3, dtype=tf.float32)
