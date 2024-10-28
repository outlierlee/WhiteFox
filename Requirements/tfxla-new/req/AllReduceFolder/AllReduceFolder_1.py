# Assume x is a tensor and ar0 and ar1 are AllReduce operations
ar0 = tf.raw_ops.AllReduce(input=x, replica_groups=[[0, 1], [2, 3]])
ar1 = tf.raw_ops.AllReduce(input=ar0, replica_groups=[[0, 2], [1, 3]])
