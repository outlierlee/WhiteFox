
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2, ..., xn):
    return tf.reduce_sum(x1) + tf.reduce_sum(x2) + ... + tf.reduce_sum(xn)

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)
x2 = tf.constant([10.,11.,12.,13.], shape=input_shape)
# ...
xn = tf.constant([100.,101.,102.,103.], shape=input_shape)

# Call model
y = m(x1, x2, ..., xn)


