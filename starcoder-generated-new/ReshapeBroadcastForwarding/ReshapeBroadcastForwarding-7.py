
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.broadcast_to(x1, [1])
    x3 = tf.reshape(x2, [])
    return x3

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant(4., shape=[])

# Call model
y = m(x1)