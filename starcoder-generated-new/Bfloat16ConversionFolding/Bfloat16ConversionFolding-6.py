

class Model(tf.keras.Model):
  def __init__(self):
    super(Model, self).__init__()
  def call(self, x1):
    x2 = tf.cast(x1, tf.bfloat16)
    return tf.cast(x2, tf.float32)

# Initializing the model
m = Model()

# Inputs to the model
input_shape=[4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)