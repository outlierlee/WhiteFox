
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x1, x2):
    y1 = tf.reduce_sum(x1)
    y2 = tf.reduce_sum(x2)
    z = tf.add(y1, y2) # binary operation should also be valid for all-reduce operations.
    return z

# Initializing the model
m = Model()

# Inputs to the model
x1 = tf.constant([4.,5.,6.,7.], shape=[4])
x2 = tf.constant([1.,2.,3.,4.], shape=[4])

# call model
z = m(x1, x2)