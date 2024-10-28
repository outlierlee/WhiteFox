
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
      x2 = tf.distribute.get_replica_context().all_reduce(tf.distribute.ReduceOp.MEAN, x1)
      x3 = strategy.run(lambda y : tf.distribute.collective_communication.all_gather(y,), args=(x2,))
    return tf.subtract(x3, x1)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```