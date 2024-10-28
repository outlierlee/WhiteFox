
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1):
    x2 = tf.multiply(x1, x1)
    return dead_computation(x2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([1.,2.,3.], shape=[3])

# Call model
y = m(x1)

# Model should create a dead computation
assert(str(y) == 'y: ()')