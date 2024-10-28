
class Model(tf.keras.Model):
    
  def __init__(self):
    super(Model, self).__init__()
    self.strategy = tf.distribute.MirroredStrategy()

  def call(self, x):
    with self.strategy.scope():
        t1 = tf.distribute.all_reduce(tf.distribute.ReduceOp.SUM, x, axis=None)
    collective_ops = tf.get_static_collection('collective_ops')
    if collective_ops:
      return True
    else:
      return False

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [3]
x = tf.constant([4., 2., 8.], shape=input_shape)

# Call model
y = m(x)