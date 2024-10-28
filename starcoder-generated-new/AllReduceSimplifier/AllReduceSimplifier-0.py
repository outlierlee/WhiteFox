
class Model(tf.keras.Model):

  def __init__(self, num_replicas, num_devices_per_replica):
    super(Model, self).__init__()
    self.num_replicas = num_replicas
    self.num_devices_per_replica = num_devices_per_replica
    strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"])
    self.init_num_replicas_sync = strategy.reduce(tf.distribute.ReduceOp.SUM, [1],
                                                  axis=None)

  def call(self, x):
    # Define tensor x
    x = tf.ones([2,2], tf.float32)
    
    # AllGather
    y = tf.distribute.all_gather(x, axis=0)
    
    # AllReduce
    with tf.distribute.get_replica_context():
      # Reducescatter
      z = tf.distribute.experimental.reducescatter(y, reduction='sum')
      # AllReduce by Add
      tf.distribute.experimental.all_reduce(z, reduction=tf.dtypes.float32.add)
      # AllReduce by Min
      tf.distribute.experimental.all_reduce(z, reduction=tf.dtypes.float32.min)
      # AllReduce by Max
      tf.distribute.experimental.all_reduce(z, reduction=tf.dtypes.float32.max)
      # AllReduce by Or
      tf.distribute.experimental.all_reduce(z, reduction=tf.dtypes.int32.bitwise_or)
      # AllReduce by And
      tf.distribute.experimental.all_reduce(z, reduction=tf.dtypes.int32.bitwise_and)
      
    return y, z

# Initializing the model
m = Model(num_replicas=2, num_devices_per_replica=1)

# Inputs to the model
x = tf.constant([4.,5.,6.,7.], shape=[2,2])

# Call model
y, z = m(x)