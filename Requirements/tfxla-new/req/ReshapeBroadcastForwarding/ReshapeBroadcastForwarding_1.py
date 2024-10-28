# Assume `input_tensor` is a scalar tensor (rank 0).
t1 = tf.broadcast_to(input_tensor, [1])
t2 = tf.reshape(t1, [])
