
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    return tf.math.multiply(tf.cast(x1, tf.float64), tf.cast(x2, tf.float64))

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([2.,3.,4.,5.], shape=input_shape)
x2 = tf.constant([6.,7.,8.,9.], shape=input_shape)

# Call model
print(m(x1, x2))