
class Model(tf.keras.Model):

  def __init__(self, dtype1, dtype2, dtype3):
    super(Model, self).__init__()
    self.dtype1 = dtype1
    self.dtype2 = dtype2
    self.dtype3 = dtype3

  def call(self, x):
    x1 = tf.cast(x, self.dtype1)
    x2 = tf.cast(x1, self.dtype2)
    return tf.cast(x2, self.dtype3)

# Initializing the model
dtype1 = tf.float32
dtype2 = tf.float16
dtype3 = tf.float32
m = Model(dtype1, dtype2, dtype3)

# Inputs to the model
input_shape = [4]
x = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x)