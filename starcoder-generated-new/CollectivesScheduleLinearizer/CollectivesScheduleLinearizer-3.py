
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    tf.distribute.experimental.set_strategy(
    tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1']))

    if tf.distribute.experimental.has_remote_tpu():
      resolver = tf.distribute.cluster_resolver.TPUClusterResolver(TPU_NAME)
      tf.config.experimental_connect_to_cluster(resolver)
      tf.tpu.experimental.initialize_tpu_system(resolver)
      strategy = tf.distribute.experimental.TPUStrategy(resolver)

    with strategy.scope():
      x = tf.distribute.AllReduce(x)
      y = tf.distribute.AllGather(x)
      return y

# Initialize the model
m = Model()

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)

# Check tpu strategy
print(tf.distribute.has_strategy())  # True