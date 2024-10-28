

class AsyncModel(tf.keras.Model):

  def __init__(self, num_replicas=2, num_partitions=1):
    super(AsyncModel, self).__init__()
    self.all_reduce = tf.raw_ops.AllReduce
    self.replicate = tf.raw_ops.AllGather
    self.num_replicas = num_replicas

  def call(self, inputs):
    with tf.device("/CPU:0"):
      all_reduce_outputs = self.all_reduce(inputs, group_key="some_key", reduce_op="ADD", control_dependencies=control_dependencies)
      gathered = self.replicate(all_reduce_outputs, num_parts=self.num_replicas, part_keys=part_keys)
    return gathered

# Initializing the model
m = AsyncModel(2, 1)

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)