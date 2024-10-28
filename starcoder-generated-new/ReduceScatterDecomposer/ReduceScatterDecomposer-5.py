:
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    input_shape = [4]
    input_tensor = tf.constant(5., shape=input_shape)
    return tf.distribute.Strategy().reduce(tf.distribute.get_replica_context().all_reduce_handle(), input_tensor)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)
```