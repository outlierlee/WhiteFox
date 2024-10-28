   # Pseudo-code to illustrate the pattern
   async_start_op = tf.raw_ops.AsyncCollectiveStart(...)
   # No significant operations here that can overlap with the async operation
   async_done_op = tf.raw_ops.AsyncCollectiveDone(async_start_op)
