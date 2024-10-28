
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.cast(x1, tf.float32)
    x3 = tf.cast(x2, tf.float64)
    x4 = tf.cast(x3, tf.uint8)
    return x4

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
dtype1 = tf.float64
dtype2 = tf.uint8
dtype3 = tf.float32
x1 = tf.cast(tf.constant(0, shape=input_shape), dtype1)

# Call model
y = m(x1)