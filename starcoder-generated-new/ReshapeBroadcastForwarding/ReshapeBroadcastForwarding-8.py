

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    x = tf.reshape(x, [1])
    return tf.reshape(x, [])

# Initializing the model
m = Model()

# Inputs to the model
x = tf.constant([2.], shape=[])

# Call model
y = m(x)


