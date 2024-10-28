
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    return tf.raw_ops.CustomCall(input_types="i", input=x1, Tout=[tf.dtypes.float32], f="Sharding")

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2, 2]
x1 = tf.constant([[1., 1.], [2., 2.]], shape=input_shape)

# Call model
y = m(x1)