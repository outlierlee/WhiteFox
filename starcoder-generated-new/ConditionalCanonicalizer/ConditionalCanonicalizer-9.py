
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    def true_fn():
      return tf.constant(0.)

    def false_fn():
      return tf.constant(1.)

    x = tf.cond(tf.constant(True), true_fn, false_fn)
    return x

# Initializing the model
m = Model()

# Inputs to the model
input_shape = [4]
x1 = tf.constant([4.,5.,6.,7.], shape=input_shape)

# Call model
y = m(x1)