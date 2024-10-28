
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x1 = tf.cast(x1, tf.bfloat16)
    return tf.cast(x1, tf.float32)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [1,1]
x1 = tf.constant([3.75], shape=input_shape, dtype=tf.float32)

# Call model
y = m(x1)