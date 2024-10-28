x = ...  # Some tensor
bcast = tf.broadcast_to(x, ...)
ag = tf.raw_ops.AllGather(input=bcast, ...)
