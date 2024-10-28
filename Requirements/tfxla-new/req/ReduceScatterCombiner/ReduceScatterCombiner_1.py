# Example pattern that might trigger the ReduceScatterCombiner
reduce_scatter_1 = tf.raw_ops.ReduceScatter(input_tensor_1, ...)
reduce_scatter_2 = tf.raw_ops.ReduceScatter(input_tensor_2, ...)
# Both reduce_scatter_1 and reduce_scatter_2 must have the same reduction operation and scatter dimension
