
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    return tf.cast(x, dtype=x.dtype)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [2]
x = tf.constant([1.,2.], shape=input_shape)

# Call model
y = m(x)