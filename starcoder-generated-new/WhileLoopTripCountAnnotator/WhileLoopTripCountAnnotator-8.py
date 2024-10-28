

Create a model with this loop pattern.

# Model
class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()

  def call(self, x):
    i = tf.constant(0)
    c = lambda i: tf.less(i, 10)
    b = lambda i: tf.add(i, 1)
    return tf.while_loop(c, b, [i])

# Initializing the model
m = Model()

# Call model
y = m(None) # This is because `TensorFlow` requires model input even though it's not used in this case


