import tensorflow as tf

# Assume `x` and `y` are tensors that are part of a distributed computation.
x = ...
y = ...

# AllReduce operations with the same reduction operation (e.g., sum).
allreduce1 = tf.raw_ops.AllReduce(input=x, reduction='sum')
allreduce2 = tf.raw_ops.AllReduce(input=y, reduction='sum')

# The model should have enough AllReduce operations to meet the threshold.
# The operations should not have layout constraints and should be consistent in domain.
