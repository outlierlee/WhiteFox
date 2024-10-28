
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.convert_to_dtype(x1, tf.float16)
    x3 = tf.slice(x2, [0,0], [2,2])
    return tf.convert_to_dtype(x3, tf.float32)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape, dtype=tf.float32)

y = m(x1)