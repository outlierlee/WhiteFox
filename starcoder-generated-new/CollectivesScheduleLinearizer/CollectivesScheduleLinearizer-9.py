
class Model(tf.keras.Model):

  def __init__(self, num_devices=4):
    super(Model, self).__init__()
    self.strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1", "/gpu:2", "/gpu:3"])
    self.all_gather_layer = tf.distribute.AllGather(self.strategy.outer_replica_id_string(), xla_replica_id=True)
    self.collective_permute_layer = tf.distribute.experimental.CollectivePermuteStart(self.strategy)
    self.async_start_layer = tf.distribute.experimental.AsyncStart(self.strategy)
    self.all_reduce_layer = tf.distribute.AllReduce(self.strategy, broadcast=True, reduce_scatter=True)

  def call(self, x1):
    return self.all_gather_layer(self.all_reduce_layer(self.async_start_layer(x1)))

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2,2]
x1 = tf.constant([[1.,0.],[1.,0.]], shape=input_shape)

# Call model
y = m(x1)

