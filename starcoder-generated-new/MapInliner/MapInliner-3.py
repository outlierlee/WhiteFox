
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    return tf.map_fn(lambda x: tf.math.square(x), x)

# Initializing the model
m = Model()
x = tf.constant([-1., 2., 3., 4.])

# Call model
y = m(x)